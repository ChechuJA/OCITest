import json
import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
EXAM_ROOT = ROOT / "Descargables" / "Microsoft"
PAGE_RE = re.compile(r"(?m)^## (?:\[)?Página (\d+)")
ANSWER_KEY_RE = re.compile(
    r"(?mi)^[ \t]*Correct Answer:[ \t]*([A-Z](?:[ \t]*,[ \t]*[A-Z])*)[ \t]*$"
)
ANSWER_HEADING_RE = re.compile(
    r"(?mi)^[ \t]*Answer(?:[ \t]+\d{2}[ \t]*[-–][ \t]*\d{2})?[ \t]*:?[ \t]*$"
)
CHOICE_RE = re.compile(r"(?m)^[ \t]{0,24}([A-Z])\.[ \t]*(.*)$")
CASE_RE = re.compile(r"(?mi)^[ \t]*CASE\s+(\d+)[^\r\n]*")


def read_source(exam_directory, basename):
    return (exam_directory / f"{basename}.extracted.md").read_text(encoding="utf-8")


def page_at(text, position):
    pages = list(PAGE_RE.finditer(text, 0, position))
    return int(pages[-1].group(1)) if pages else 1


def remove_page_headers(text):
    return re.sub(r"(?m)^## (?:\[)?Página \d+[^\r\n]*\r?\n?", "", text)


def clean_text(text):
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line and line != "---").strip()


def pdf_link(exam_id, filename, page):
    encoded = quote(filename, safe="-._")
    return f"Descargables/Microsoft/{exam_id.upper()}/{encoded}#page={page}"


def parse_options(question_text):
    matches = list(CHOICE_RE.finditer(question_text))
    if len(matches) < 2:
        return clean_text(question_text), []

    prompt = question_text[:matches[0].start()]
    options = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(question_text)
        continuation = " ".join(
            line.strip()
            for line in question_text[match.end():end].splitlines()
            if line.strip() and line.strip() != "---"
        )
        content = " ".join(part for part in (match.group(2).strip(), continuation) if part)
        options.append({"key": match.group(1).upper(), "text": content})
    return clean_text(prompt), options


def explanation_from_block(block, answer_heading, answer_key):
    start = answer_heading.end() if answer_heading else (answer_key.start() if answer_key else len(block))
    explanation = remove_page_headers(block[start:])
    explanation = re.sub(
        r"(?mi)^[ \t]*Correct Answer:[^\r\n]*", "", explanation
    )
    explanation = re.sub(
        r"(?mi)^[ \t]*Explanation:[ \t]*", "", explanation
    )
    return clean_text(explanation)


def make_question(question_id, prompt, options, correct_keys, explanation, source_link):
    option_keys = {option["key"] for option in options}
    valid_keys = bool(correct_keys) and set(correct_keys).issubset(option_keys)
    answer_keys = correct_keys if valid_keys else []
    explanation = explanation.strip()
    explanation = f"{explanation}\n\nFuente: {source_link}" if explanation else f"Fuente: {source_link}"
    question = {
        "id": question_id,
        "question": prompt or "Consulta esta pregunta en el PDF original.",
        "answers": options,
        "correctKeys": answer_keys,
        "explanation": explanation,
    }
    if not valid_keys:
        question["ungraded"] = True
    return question


def parse_question_section(text, exam_id, source_filename, marker_pattern, case_mode=False):
    exam_directory = EXAM_ROOT / exam_id.upper()
    markers = list(re.finditer(marker_pattern, text))
    case_starts = list(CASE_RE.finditer(text)) if case_mode else []
    questions = []

    for index, marker in enumerate(markers):
        end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
        block = text[marker.end():end]
        answer_key = ANSWER_KEY_RE.search(block)
        answer_heading = ANSWER_HEADING_RE.search(block)
        question_end = answer_heading.start() if answer_heading else (answer_key.start() if answer_key else len(block))
        prompt, options = parse_options(remove_page_headers(block[:question_end]))

        if case_mode:
            current_case = next((item for item in reversed(case_starts) if item.start() < marker.start()), None)
            if current_case:
                first_question = next(
                    (item for item in markers if item.start() > current_case.end()), marker
                )
                scenario = clean_text(remove_page_headers(text[current_case.end():first_question.start()]))
                case_number = re.search(r"\d+", current_case.group(1)).group(0)
                question_number = "-".join(marker.groups()[:2])
                prompt = f"Case {case_number}, pregunta {question_number}:\n{scenario}\n\n{prompt}"

        correct_keys = (
            [key.strip().upper() for key in answer_key.group(1).split(",")]
            if answer_key
            else []
        )
        explanation = explanation_from_block(block, answer_heading, answer_key)
        source_page = page_at(text, marker.start())
        source_link = pdf_link(exam_id, source_filename, source_page)
        question_id = marker.group(1) if not case_mode else f"{marker.group(1)}-{marker.group(2)}"
        questions.append(
            make_question(question_id, prompt, options, correct_keys, explanation, source_link)
        )

    return questions


def multi_verdict(text):
    explicit = re.search(r"(?i)Correct answer:[ \t]*([AB])[.]?[ \t]*(Yes|No)?", text)
    if explicit:
        if explicit.group(2):
            return explicit.group(2).lower() == "yes"
        return explicit.group(1).upper() == "A"

    patterns = [
        (False, r"\b(?:does not|do not|doesn't|don't|cannot|can't|fails? to|is not|isn't)\s+(?:fully\s+)?(?:meet|satisfy|achieve|fulfill|provide|customize|allow|ensure|support)\b"),
        (False, r"\bnot\s+(?:meet|satisfy|achieve|fulfill|provide|customize|allow|ensure|support)\s+(?:the\s+)?(?:goal|requirement|requirements|capability)\b"),
        (True, r"\b(?:does\s+meet|meets|satisfies|achieves|fulfills|supports)\s+(?:the\s+)?(?:stated\s+)?(?:goal|requirement|requirements)\b"),
        (True, r"\bsolution\s+meets\s+(?:the\s+)?(?:goal|requirement|requirements)\b"),
    ]
    matches = [
        (match.start(), value)
        for value, pattern in patterns
        for match in re.finditer(pattern, text, re.IGNORECASE)
    ]
    return max(matches)[1] if matches else None


def parse_multi_section(text, exam_id, source_filename):
    exam_directory = EXAM_ROOT / exam_id.upper()
    scenario_markers = list(re.finditer(r"(?mi)^[ \t]*MULTI\s+(\d+)[^\r\n]*", text))
    option_pattern = re.compile(r"(?mi)^[ \t]*Option\s*(\d+):?[ \t]*$")
    questions = []

    for scenario_index, marker in enumerate(scenario_markers):
        end = scenario_markers[scenario_index + 1].start() if scenario_index + 1 < len(scenario_markers) else len(text)
        block = text[marker.end():end]
        options = list(option_pattern.finditer(block))
        scenario = clean_text(remove_page_headers(block[:options[0].start()])) if options else clean_text(block)

        for option_index, option_marker in enumerate(options):
            option_end = options[option_index + 1].start() if option_index + 1 < len(options) else len(block)
            option_block = remove_page_headers(block[option_marker.end():option_end])
            solution = re.search(r"(?im)^[ \t]*Solution:[ \t]*(.*)$", option_block)
            question_end = re.search(r"(?im)^[ \t]*Does this meet the goal\?[ \t]*$", option_block)
            prompt_end = question_end.start() if question_end else len(option_block)
            solution_text = clean_text(option_block[solution.start():prompt_end]) if solution else ""
            rationale = option_block[question_end.end():] if question_end else ""
            verdict = multi_verdict(rationale)
            correct_keys = ["A" if verdict else "B"] if verdict is not None else []
            source_page = page_at(text, marker.start() + option_marker.start())
            source_link = pdf_link(exam_id, source_filename, source_page)
            prompt = (
                f"MULTI {marker.group(1)}, propuesta {option_marker.group(1)}:\n"
                f"{scenario}\n\n{solution_text}\n¿Cumple el objetivo?"
            )
            questions.append(
                make_question(
                    f"{marker.group(1)}-{option_marker.group(1)}",
                    prompt,
                    [{"key": "A", "text": "Sí"}, {"key": "B", "text": "No"}],
                    correct_keys,
                    clean_text(rationale),
                    source_link,
                )
            )

    return questions


def save_section(exam_id, section_id, questions):
    path = EXAM_ROOT / exam_id.upper() / f"{exam_id.lower()}-{section_id}.json"
    path.write_text(json.dumps(questions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    gradable = sum(not question.get("ungraded", False) for question in questions)
    print(f"{exam_id.upper()} {section_id}: {len(questions)} preguntas ({gradable} puntuables)")
    return path.relative_to(ROOT).as_posix()


def convert_exam(exam_id, filenames, qa_pattern, cases_pattern, expected):
    directory = EXAM_ROOT / exam_id.upper()
    qa_text = read_source(directory, filenames["qa"])
    cases_text = read_source(directory, filenames["cases"])
    multi_text = read_source(directory, filenames["multi"])

    sections = {
        "qa": parse_question_section(qa_text, exam_id, filenames["qa_pdf"], qa_pattern),
        "multi": parse_multi_section(multi_text, exam_id, filenames["multi_pdf"]),
        "cases": parse_question_section(
            cases_text, exam_id, filenames["cases_pdf"], cases_pattern, case_mode=True
        ),
    }

    actual = {section: len(questions) for section, questions in sections.items()}
    if actual != expected:
        raise ValueError(f"{exam_id.upper()} count mismatch: expected {expected}, got {actual}")

    paths = {
        section_id: save_section(exam_id, section_id, questions)
        for section_id, questions in sections.items()
    }
    total = sum(actual.values())
    aggregate_name = f"{exam_id.replace('-', '')}-questions.json"
    aggregate_path = directory / aggregate_name
    aggregate = [question for section in sections.values() for question in section]
    aggregate_path.write_text(
        json.dumps(aggregate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    paths["all"] = aggregate_path.relative_to(ROOT).as_posix()
    print(f"{exam_id.upper()} total: {total} preguntas; ficheros: {paths}")
    return total, paths, actual


def main():
    convert_exam(
        "pl-200",
        {
            "qa": "PL-200 Q&A",
            "cases": "PL-200-CASES",
            "multi": "PL-200-MULTI",
            "qa_pdf": "PL-200 Q&A.pdf",
            "cases_pdf": "PL-200-CASES.pdf",
            "multi_pdf": "PL-200-MULTI.pdf",
        },
        r"(?m)^[ \t]*(\d{3}) Question\.[ \t]*$",
        r"(?mi)^[ \t]*Question\s+(\d{2})\s*[–-]\s*(\d{2})[ \t]*$",
        {"qa": 185, "multi": 36, "cases": 47},
    )
    convert_exam(
        "ab-100",
        {
            "qa": "AB-100-QA",
            "cases": "AB-100-CASES",
            "multi": "AB-100-MULTI",
            "qa_pdf": "AB-100 Q&A.pdf",
            "cases_pdf": "AB-100-CASES.pdf",
            "multi_pdf": "AB-100-MULTI.pdf",
        },
        r"(?m)^[ \t]*(\d{3}) Question\.[ \t]*$",
        r"(?mi)^[ \t]*Question\s+(\d{2})\s*[–-]\s*(\d{2})[ \t]*$",
        {"qa": 85, "multi": 10, "cases": 16},
    )


if __name__ == "__main__":
    main()