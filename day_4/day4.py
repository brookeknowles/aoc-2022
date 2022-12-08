counter_part_1 = 0
counter_part_2 = 0

with open("input.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        a, b = line.split(",")

        a_pair = [int(i) for i in a.split("-")]
        b_pair = [int(i) for i in b.split("-")]

        a_list = list(range(a_pair[0], a_pair[1] + 1))
        b_list = list(range(b_pair[0], b_pair[1] + 1))

        # checks if a pair is fully contained in another (part 1)
        if (set(a_list).issubset(set(b_list))) or (set(b_list).issubset(set(a_list))):
            counter_part_1 += 1

        # checks if there is any overlap at all (part 2)
        if any(i in a_list for i in b_list):
            counter_part_2 += 1


print(f"pairs that fully contain the other (part 1) = {counter_part_1}")
print(f"pairs that have any part of another (part 2) = {counter_part_2}")

