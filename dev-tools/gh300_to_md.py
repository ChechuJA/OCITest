#!/usr/bin/env python3
import json
from pathlib import Path

SRC = Path(r"c:\Github\OCITest\Descargables\GH-300\gh300-questions.json")
DST = Path(r"c:\Github\OCITest\Descargables\GH-300\gh300-questions.md")


def main() -> int:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("Expected a JSON array")

    lines: list[str] = []
    lines.append("# GH-300 — GitHub Copilot (exportado desde JSON)")
    lines.append("")
    lines.append(f"Fuente: {SRC.name}")
    lines.append(f"Total preguntas: {len(data)}")
    lines.append("")

    for item in data:
        qid = item.get("id")
        question = (item.get("question") or "").strip()
        answers = item.get("answers") or []
        correct = set((k or "").strip().upper() for k in (item.get("correctKeys") or []))

        if not question or not answers:
            continue

        lines.append(f"#### Q{qid}. {question}")

        # Orden estable por letra
        answers_sorted = sorted(
            (
                {
                    "key": str(a.get("key", "")).strip().upper(),
                    "text": str(a.get("text", "")).strip(),
                }
                for a in answers
            ),
            key=lambda a: a["key"],
        )

        for a in answers_sorted:
            if not a["key"] or not a["text"]:
                continue
            mark = "x" if a["key"] in correct else " "
            lines.append(f"- [{mark}] {a['text']}")

        lines.append("")

    DST.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {DST} ({DST.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
