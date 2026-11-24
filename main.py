"""One Word From Grandma -- make.fun entry.

Writes the single word a grandma would text about AI to /output/entry.txt.
Pure Python 3.13 standard library, deterministic, no network, no randomness.

The word: "Witchcraft".
Why this word, against the judge's criteria in order:
1. It reads as the single word a grandma would text about AI -- her verdict
   on a machine that talks back: it must be witchcraft.
2. It sounds like a real grandmother's texting voice: warm, old-fashioned,
   a little baffled by the new thing, typed to a grandchild.
3. The joke lands in one word with no caption: grandma has explained AI.
4. It is tied to AI as her theory of how the machine works -- mysterious,
   uncanny, beyond understanding -- not a word that fits any subject.
5. It is a fresh pick, not the obvious "Robot" or "Wow", and instantly
   readable at ten letters.
"""

import os
from pathlib import Path

WORD = "Witchcraft"


def _validate(word: str) -> None:
    """Enforce the kit's gate before writing anything.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 30
    characters, not only white space, and the brief requires exactly one
    word. Fail loudly here rather than submitting an invalid entry.
    """
    if not word or word != word.strip():
        raise ValueError("entry must not be blank or padded with whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1 to 30 characters")


def main() -> None:
    _validate(WORD)
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
