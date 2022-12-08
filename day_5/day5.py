instructions = []
stacks = [] # 2d array

with open("test.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        if "move" in line:
            instructions.append(line)

print(instructions)