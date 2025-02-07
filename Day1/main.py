from collections import Counter

with open("Inputs/input", "r") as file:
    left_list = []
    right_list = []

    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)


def part1(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    print("Total Distance:", total_distance)
    return total_distance


def part2(left_list, right_list):
    right_count = Counter(right_list)

    total_sum = sum(value * right_count[value] for value in left_list)
    print("Similarity score:", +total_sum)
    return total_sum


sum_1 = part1(left_list, right_list)
sum_2 = part2(left_list, right_list)

# TODO: Learn about ZIP
