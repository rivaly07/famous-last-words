import os, pathlib
EPITAPH = "Don't worry, I fixed the wiring myself. Watch this."
def main():
    out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or ("/output" if pathlib.Path("/output").is_dir() else "out"))
    out.mkdir(parents=True, exist_ok=True)
    line = EPITAPH.strip()
    assert 1 <= len(line) <= 150 and "\n" not in line
    (out / "entry.txt").write_text(line, encoding="utf-8")
    print(line, len(line))
if __name__ == "__main__":
    main()
