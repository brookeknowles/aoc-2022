"""
answers for day 3
"""

def get_type_in_both_compartments(str1, str2):
    """ Given 2 strings gets the character they have in common """
    for x in str1:
        for y in str2:
            if x == y:
                return x
    return 0    # no similar chars found

def get_priority(t):
    """ 
    given a type, returns the priority of that type. 
    yes this is very ugly code 
    """
    if t == 'a':
        return 1
    elif t == 'b':
        return 2
    elif t == 'c':
        return 3
    elif t == 'd':
        return 4
    elif t == 'e':
        return 5
    elif t == 'f':
        return 6
    elif t == 'g':
        return 7
    elif t == 'h':
        return 8
    elif t == 'i':
        return 9
    elif t == 'j':
        return 10
    elif t == 'k':
        return 11
    elif t == 'l':
        return 12
    elif t == 'm':
        return 13
    elif t == 'n':
        return 14
    elif t == 'o':
        return 15
    elif t == 'p':
        return 16
    elif t == 'q':
        return 17
    elif t == 'r':
        return 18
    elif t == 's':
        return 19
    elif t == 't':
        return 20
    elif t == 'u':
        return 21
    elif t == 'v':
        return 22
    elif t == 'w':
        return 23
    elif t == 'x':
        return 24
    elif t == 'y':
        return 25
    elif t == 'z':
        return 26
    if t == 'A':
        return 1 + 26 
    elif t == 'B':
        return 2 + 26
    elif t == 'C':
        return 3 + 26
    elif t == 'D':
        return 4 + 26
    elif t == 'E':
        return 5 + 26
    elif t == 'F':
        return 6 + 26
    elif t == 'G':
        return 7 + 26
    elif t == 'H':
        return 8 + 26
    elif t == 'I':
        return 9 + 26
    elif t == 'J':
        return 10 + 26
    elif t == 'K':
        return 11 + 26
    elif t == 'L':
        return 12 + 26
    elif t == 'M':
        return 13 + 26
    elif t == 'N':
        return 14 + 26
    elif t == 'O':
        return 15 + 26
    elif t == 'P':
        return 16 + 26
    elif t == 'Q':
        return 17 + 26
    elif t == 'R':
        return 18 + 26
    elif t == 'S':
        return 19 + 26
    elif t == 'T':
        return 20 + 26
    elif t == 'U':
        return 21 + 26
    elif t == 'V':
        return 22 + 26
    elif t == 'W':
        return 23 + 26
    elif t == 'X':
        return 24 + 26
    elif t == 'Y':
        return 25 + 26
    elif t == 'Z':
        return 26 + 26

sum_of_priorities = 0
with open("input.txt") as file:
    for line in file:
        line = line.replace("\n", "")   # get rid of the ugly \n

        first_compartment  = line[:len(line)//2]
        second_compartment = line[len(line)//2:]

        common_type = get_type_in_both_compartments(first_compartment, second_compartment)

        priority = get_priority(common_type)        
        sum_of_priorities += priority

print("Total sum of priorities (part 1) = ", sum_of_priorities)

# second half of puzzle

def get_badge(str1, str2, str3):
    """ Given 3 strings gets the character they have in common """
    for x in str1:
        for y in str2:
            for z in str3:
                if x == y and y == z:
                    return x
    return 0    # no similar chars found


sum_of_priorities = 0
with open("input.txt") as file:
    line_number = 0
    group = []
    for line in file:
        line = line.replace("\n", "")   # get rid of the ugly \n
        group.append(line)  # add to seperate list so can eval in groups of 3
        line_number += 1

        if (line_number > 2):
            # we have a group. time to test for the badge and priority
            badge = get_badge(group[0], group[1], group[2])
            priority = get_priority(badge)
            sum_of_priorities += priority

            # clear the group, go back to loop to get next group
            line_number = 0
            group = []
        
print("Total sum of priorities (part 2) = ", sum_of_priorities)