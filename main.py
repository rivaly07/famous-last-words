import os
from pathlib import Path

EPITAPH = "Don't worry, I fixed the wiring myself. Watch this."


def main():
    configured_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured_dir:
        output_dir = Path(configured_dir)
    elif Path("/output").is_dir():
        output_dir = Path("/output")
    else:
        output_dir = Path("./out")

    output_dir.mkdir(parents=True, exist_ok=True)
    line = EPITAPH
    if not 1 <= len(line) <= 150:
        raise ValueError("epitaph must be between 1 and 150 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("epitaph must be a single line")
    if not line.strip():
        raise ValueError("epitaph must contain non-whitespace text")

    (output_dir / "entry.txt").write_text(line, encoding="utf-8")
    print(line, len(line))


if __name__ == "__main__":
    main()
