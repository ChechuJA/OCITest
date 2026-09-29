"""Completa las explicaciones de los JSON a partir de sus documentos Word."""

import json
import re
from pathlib import Path

from docx import Document


ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    (
        ROOT / "Descargables/Terraform/004/source/HASHICORP TERRAFORM - 004.docx",
        ROOT / "Descargables/Terraform/004/terraform-questions.json",
    ),
    (
        ROOT / "Descargables/Vault/source/Vault 002 1.docx",
        ROOT / "Descargables/Vault/vault-questions.json",
    ),
]


def normalize(value):
    return re.sub(r"\s+", " ", value or "").strip().lower()


def get_docx_blocks(docx_path):
    paragraphs = [paragraph.text.strip() for paragraph in Document(docx_path).paragraphs]
    starts = [
        index for index, text in enumerate(paragraphs)
        if text.lower().startswith("question")
    ]
    blocks = []
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(paragraphs)
        block = paragraphs[start:end]
        try:
            answer_index = next(i for i, text in enumerate(block) if text.lower() == "answer")
        except StopIteration:
            continue
        try:
            explanation_index = next(
                i for i, text in enumerate(block[answer_index:], answer_index)
                if text.lower().startswith("explanation:")
            )
        except StopIteration:
            continue

        discussion_index = next(
            (
                i for i, text in enumerate(block[explanation_index + 1:], explanation_index + 1)
                if text.lower().startswith("discussion:")
            ),
            len(block),
        )
        discussion = block[discussion_index].split(":", 1)[1].strip() if discussion_index < len(block) else ""
        explanation = " ".join(block[explanation_index + 1:discussion_index]).strip()
        question_text = " ".join(block[1:answer_index]).strip()
        blocks.append({
            "question": normalize(question_text),
            "explanation": explanation,
            "discussion": discussion,
        })
    return blocks


def find_block(question, blocks, used):
    question_key = normalize(question)
    prefix = question_key[:100]
    candidates = [
        (index, block) for index, block in enumerate(blocks)
        if index not in used and prefix and prefix in block["question"]
    ]
    if not candidates:
        return None
    return candidates[0]


def enrich(docx_path, json_path):
    blocks = get_docx_blocks(docx_path)
    questions = json.loads(json_path.read_text(encoding="utf-8"))
    used = set()
    matched = 0

    for question in questions:
        result = find_block(question.get("question", ""), blocks, used)
        if result is None:
            continue
        index, block = result
        used.add(index)
        parts = [part for part in (block["explanation"], f'Discussion: {block["discussion"]}' if block["discussion"] else "") if part]
        if parts:
            question["explanation"] = "\n\n".join(parts)
            matched += 1

    json_path.write_text(json.dumps(questions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{json_path.name}: {matched}/{len(questions)} explicaciones actualizadas")


if __name__ == "__main__":
    for docx_path, json_path in SOURCES:
        enrich(docx_path, json_path)