import sys
from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """Perform iterative binary search on a sorted list.
    
    Returns the 0-based index if target is found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main() -> None:
    # Read tokens from standard input to handle single or multiple queries cleanly
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    idx = 0
    while idx < len(tokens):
        n = int(tokens[idx])
        idx += 1
        arr = [int(tokens[idx + i]) for i in range(n)]
        idx += n
        target = int(tokens[idx])
        idx += 1

        result = binary_search(arr, target)
        print(result)


if __name__ == "__main__":
    main()

