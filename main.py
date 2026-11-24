import os

TEXT = (
    "My alarm clock has exactly one job, and it outsources it to the "
    "snooze button nine times every single morning."
)


def main() -> None:
    # Self-check against the gate: 1 to 200 characters, not only whitespace.
    assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} code points"
    assert TEXT.strip(), "entry is only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
