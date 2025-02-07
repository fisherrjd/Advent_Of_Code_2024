# SMALL INPUT               There is 1 report per line
# 7 6 4 2 1                 ~good~ IF
# 1 2 7 8 9                 All increasing || Decreasing
# 9 7 6 2 1                 rerport[n+1] +- 3 && != reprot[n]
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9


# Ways to solve
# Grab per report
with open("Inputs/input_small", "r") as file:
    report = []

    for line in file:
        print("line:", line)
        list = map(int, line.strip().split())
        print("list:", list)
        report.append(list)

print(report)

# def part1():
