import os


def part1(reports):
    for report in reports:
        print(report)  # Debugging: Print the full report
        value = None
        for prev, curr in zip(
            report, report[1:]
        ):  # Compare pairs of consecutive values
            if curr > prev:
                print(f"{curr} is greater than {prev}")


# TODO:
# Implement check for all increasing / decreasing
#  - use a flag?


# SMALL INPUT               There is 1 report per line
# 7 6 4 2 1                 ~good~ IF
# 1 2 7 8 9                 All increasing || Decreasing
# 9 7 6 2 1                 report[n+1] +- 3 && != report[n]
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# Call main() to execute the script
