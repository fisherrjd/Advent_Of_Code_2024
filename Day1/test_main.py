import pytest
from main import part1, part2

with open("/aoc2024/Day1/Inputs/input", "r") as file:
    left_list = []
    right_list = []

    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)


def test_part1(self):
    expected = 2344935
    result = part1(left_list, right_list)
    assert result == expected, f"Expected {expected}, got {result}"


def test_part2(self):
    expected = 27647262
    result = part2(left_list, right_list)
    assert result == expected, f"Expected {expected}, got {result}"
