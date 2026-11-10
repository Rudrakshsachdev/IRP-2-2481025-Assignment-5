# IRP2 Assignment – Python Programming

- **Student Name:** Rudraksh Sachdeva
- **Roll Number:** 2481025
- **Course:** B.Tech CSE (AI & ML)

---

## Project Overview

This repository contains solutions and automated test suites for the **IRP2 Python Programming Assignment**. The assignment focuses on core algorithmic problem solving, clean code architecture, recursion, and search algorithms implemented in Python 3 without external libraries.

---

## Project Structure

```text
.
├── .gitignore
├── README.md
├── problems/
│   ├── p1_reverse_words.py     # Problem 1: Reverse Word Order
│   ├── p2_binary_search.py     # Problem 2: Manual Binary Search (0-based index or -1)
│   ├── p3_digit_sum.py         # Problem 3: Recursive Digit Sum
│   └── p4_pair_count.py        # Problem 4: Pair Count (Pending condition)
└── tests/
    ├── p1_input.txt            # Test inputs for Problem 1
    ├── p1_expected.txt         # Expected outputs for Problem 1
    ├── p2_input.txt            # Test inputs for Problem 2
    ├── p2_expected.txt         # Expected outputs for Problem 2
    ├── p3_input.txt            # Test inputs for Problem 3
    ├── p3_expected.txt         # Expected outputs for Problem 3
    ├── p4_input.txt            # Test inputs for Problem 4
    └── p4_expected.txt         # Expected outputs for Problem 4
```

---

## Requirements

- **Python Version:** Python 3.8+ (tested on Python 3.13)
- No third-party packages or external dependencies required.

---

## Execution Instructions

All programs read from standard input (`sys.stdin`) and write directly to standard output (`sys.stdout`).

### Running Programs Directly (Interactive Mode)

```bash
python problems/p1_reverse_words.py
python problems/p2_binary_search.py
python problems/p3_digit_sum.py
python problems/p4_pair_count.py
```

---

## Testing with Input Redirection

You can run each problem against the test suite using input redirection or pipes:

### Command Prompt (cmd) / Bash / Linux / macOS

```bash
python problems/p1_reverse_words.py < tests/p1_input.txt
python problems/p2_binary_search.py < tests/p2_input.txt
python problems/p3_digit_sum.py < tests/p3_input.txt
python problems/p4_pair_count.py < tests/p4_input.txt
```

### PowerShell (Windows)

In PowerShell, use `Get-Content` piped into Python:

```powershell
Get-Content tests/p1_input.txt | python problems/p1_reverse_words.py
Get-Content tests/p2_input.txt | python problems/p2_binary_search.py
Get-Content tests/p3_input.txt | python problems/p3_digit_sum.py
Get-Content tests/p4_input.txt | python problems/p4_pair_count.py
```

---

## Problem Summaries

### Problem 1: Reverse Word Order

- **File:** [p1_reverse_words.py](file:///c:/IRP/problems/p1_reverse_words.py)
- **Description:** Reverses the sequence of words in a sentence while keeping individual word spellings intact.

### Problem 2: Binary Search

- **File:** [p2_binary_search.py](file:///c:/IRP/problems/p2_binary_search.py)
- **Description:** Implements an iterative binary search manually (without built-in search methods) over a sorted list of integers to find a target value. Returns the 0-based index or `-1` if not found.

### Problem 3: Recursive Digit Sum

- **File:** [p3_digit_sum.py](file:///c:/IRP/problems/p3_digit_sum.py)
- **Description:** Computes the sum of digits of a given integer using pure recursion without any loops.

### Problem 4: Pair Count

- **File:** [p4_pair_count.py](file:///c:/IRP/problems/p4_pair_count.py)
- **Description:** Counts pairs of elements meeting the specified condition.
