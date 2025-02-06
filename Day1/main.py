with open("input", "r") as file:
    left_list = []
    right_list = []

    for line in file:
        left,right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

print("Left List:", left_list)
print("Right List:", right_list)

left_list.sort()
right_list.sort()

print("Left List:", left_list)
print("Right List:", right_list)

# TODO: Learn about ZIP
total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
print("Total Distance:", total_distance)
