import sys
from typing import List


def count_pairs_with_sum(arr: List[int], target_sum: int) -> int:
    """Count pairs of indices (i, j) with i < j such that arr[i] + arr[j] == target_sum.
    
    Uses a frequency dictionary to achieve an optimal O(n) time complexity
    and O(n) auxiliary space.
    """
    freq = {}
    pair_count = 0

    for num in arr:
        complement = target_sum - num
        if complement in freq:
            pair_count += freq[complement]
        freq[num] = freq.get(num, 0) + 1

    return pair_count


def main() -> None:
    # Read all tokens from standard input
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    idx = 0
    while idx < len(tokens):
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2

        arr = [int(tokens[idx + i]) for i in range(n)]
        idx += n

        result = count_pairs_with_sum(arr, k)
        print(result)


if __name__ == "__main__":
    main()
