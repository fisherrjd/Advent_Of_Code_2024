from collections import Counter


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


# TODO: Learn about ZIP
