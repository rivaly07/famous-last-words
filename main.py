"""Write one UTF-8 famous-last-words epitaph (1–150 characters) for the judge."""

import os
from pathlib import Path

EPITAPH = "Don't worry, I fixed the wiring myself. Watch this."


def output_directory() -> Path:
    """Use the configured output, /output when available, or this repo's ./out."""
    if "MAKEFUN_OUTPUT_DIR" in os.environ:
        return Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    harness_output = Path("/output")
    if harness_output.is_dir():
        return harness_output
    return Path(__file__).resolve().parent / "out"


def main() -> None:
    assert 1 <= len(EPITAPH) <= 150, "epitaph must be 1 to 150 characters"
    assert "\n" not in EPITAPH and "\r" not in EPITAPH, "epitaph must be one line"
    assert EPITAPH.strip(), "epitaph must not be only whitespace"

    destination = output_directory()
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_text(EPITAPH, encoding="utf-8", newline="")
    print(EPITAPH)
    print(len(EPITAPH))


if __name__ == "__main__":
    main()
