import sys


def digit_sum_recursive(n: int) -> int:
    """Calculate the sum of digits of a non-negative integer using recursion only.
    
    Base case: when n < 10, the sum of its digits is simply n itself.
    Recursive step: last digit (n % 10) + digit sum of remaining digits (n // 10).
    """
    if n < 10:
        return n
    return (n % 10) + digit_sum_recursive(n // 10)


def main() -> None:
    tokens = sys.stdin.read().split()
    for token in tokens:
        # Handle possible negative integers by taking absolute value
        number = abs(int(token))
        result = digit_sum_recursive(number)
        print(result)


if __name__ == "__main__":
    main()

