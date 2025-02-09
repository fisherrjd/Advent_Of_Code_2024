import pytest
from main import part1, part2
from typing import List

# Read input and populate lists
with open("Day1/Inputs/input", "r") as file:
    left_list: List[int] = [1]
    right_list: List[int] = []

    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)


def test_part1() -> None:
    expected: int = 2386409
    result: int = part1(left_list, right_list)
    print(result)
    assert result == expected, f"Expected {expected}, got {result}"


def test_part2() -> None:
    expected: int = 27647262
    result: int = part2(left_list, right_list)
    print(result)
    assert result == expected, f"Expected {expected}, got {result}"
