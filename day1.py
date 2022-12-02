"""
Answers for day 1
"""

# will store total calories for each elf i.e. total_calories[0] = 1000 means elf 1 has 1000 calories total, total_calories[2] = 2000 means elf 2 has 2000 calories total etc
total_calories = []
elf_cals_total = 0

with open("input.txt") as file:
    for line in file:
        if line == "\n":
            total_calories.append(elf_cals_total)
            elf_cals_total = 0
        else:
            elf_cals_total += int(line)

most_cals_single_elf = max(total_calories)

print("Answer to the first half: ", most_cals_single_elf)

# for the 2nd half
top_3_total = 0

for i in range(3):
    most_cals_single_elf = max(total_calories)      # find the next maximum
    max_index = [index for index, item in enumerate(total_calories) if item == most_cals_single_elf][0] # find index of the max
    total_calories[max_index] = 0                   # make value at that index 0 (so itll no longer be counted as the highest number)
    top_3_total += most_cals_single_elf             # add the max to the counter

print("Answer to the second half: ", top_3_total)
