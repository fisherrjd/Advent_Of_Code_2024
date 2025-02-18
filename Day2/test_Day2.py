import pytest
import os
from main import part1


def getReports():
    file_path = os.path.join("Inputs", "input_small")
    # Read and process the file
    with open(file_path, "r") as file:
        reports = []

        for line in file:
            stripped_line = line.strip()

            # Debugging
            print(stripped_line)

            if not stripped_line:
                continue

            report = [int(x) for x in stripped_line.split()]
            reports.append(report)
    return reports


def test_part1():
    part1(getReports())
    print("success")


def test_part2():
    print("success")


test_part1()
test_part2()
