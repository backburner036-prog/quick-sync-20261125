"""Entry for make.fun bounty "Make the AI Judge Laugh".

One line about office life: the 15-minute "quick sync" that runs to minute
47. The joke is built on the laugh recipe — a relatable scene, one specific
named detail, and an absurd closer in the last beat:

  1. Relatable scene: the "quick sync" every office worker has sat in.
  2. Specific detail: "15-minute" vs "minute 47", and zero decisions.
  3. Absurd closer: the meeting about saving time spawns three follow-up
     meetings — the time-saving meeting breeds more meetings.

Delete the last sentence and the joke loses its meaning: the escalation
is the punchline, not decoration. 104 characters, under the 200 cap.

Why each word earns its place (laugh recipe, beat by beat):
  - "15-minute" is the promise the meeting itself makes — the label on the
    invite, not the narrator's claim. The number is the setup's contract.
  - "hit minute 47" breaks that contract with a second, larger number:
    the gap between 15 and 47 is the whole joke's engine, no adjective
    needed. Concrete numbers beat adjectives; the reader does the math.
  - "zero decisions" is the middle beat: time spent, nothing decided.
    It turns a long meeting into a failed meeting, which is funnier.
  - "spawned three follow-up meetings" is the absurd closer: the meeting
    whose purpose was saving time breeds more meetings. Cause and effect
    are inverted — the cure produces the disease. That inversion is the
    twist, and it lands in the last beat, where the winner pattern says
    it must. No pun, no stock line, no "Monday blues": the premise is
    fresh because the escalation is structural, not verbal.
"""

from pathlib import Path

TEXT = "Our 15-minute 'quick sync' hit minute 47, produced zero decisions, and spawned three follow-up meetings."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not whitespace only."""
    text.encode("utf-8")
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
