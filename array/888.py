"""https://leetcode.com/problems/fair-candy-swap/."""
from typing import List
from utils import run


def solution(a: List[int], b: List[int]) -> List[int]:
    a_sum = sum(a)
    b_sum = sum(b)

    for i in range(len(a)):
        for j in range(len(b)):
            swap_a_sum = a_sum - a[i] + b[j]
            swap_b_sum = b_sum - b[j] + a[i]
            print((a[i], b[j]), swap_a_sum, swap_b_sum)
            if swap_a_sum == swap_b_sum:
                return [a[i], b[j]]


if __name__ == "__main__":
    test_cases = [
        {
            "input": {"a": [4, 1, 2, 1, 1, 2], "b": [3, 6, 3, 3]},
            "ans": (1, 3)
        },
        {
            "input": {"a": [5, 7, 4, 6], "b": [1, 2, 3, 8]},
            "ans": (6, 2)
        }
    ]
    run(test_cases, solution)
