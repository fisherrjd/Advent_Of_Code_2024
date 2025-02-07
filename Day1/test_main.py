import pytest
from main import part1, part2

with open("./Day1/Inputs/input", "r") as file:
    left_list = [1]
    right_list = []

    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)


def test_part1():
    expected = 2344935
    result = part1(left_list, right_list)
    print(result)
    assert result == expected, f"Expected {expected}, got {result}"


def test_part2():
    expected = 27647262
    result = part2(left_list, right_list)
    print(result)
    assert result == expected, f"Expected {expected}, got {result}"
