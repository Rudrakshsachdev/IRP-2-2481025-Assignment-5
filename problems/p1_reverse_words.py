import sys


def reverse_words(text: str) -> str:
    """Reverse the order of words in the given text while preserving individual words."""
    words = text.split()
    return " ".join(reversed(words))


def main() -> None:
    # Read all lines from standard input to handle multi-line or batch test cases
    input_data = sys.stdin.read().splitlines()
    for line in input_data:
        # Process each line independently; print reversed words
        if line.strip():
            print(reverse_words(line))
        else:
            print("")


if __name__ == "__main__":
    main()

