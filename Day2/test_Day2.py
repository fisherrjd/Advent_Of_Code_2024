import pytest

with open("Day2/Inputs/input_small", "r") as file:
    reports = []

    for line in file:
        print("line:", line.strip())  # Debugging
        reports.append([int(x) for x in line.split()])

print("test:", reports)
