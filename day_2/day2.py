"""
answers for day 2
"""
def check_winner(game):
    rock = "AX"
    paper = "BY"
    scissors = "CZ"
    if game[0] in rock and game[1] in rock:
        return 3
    if game[0] in paper and game[1] in paper:
        return 3
    if game[0] in scissors and game[1] in scissors:
        return 3
    elif game[0] in rock and game[1] in scissors:
        return 0
    elif game[0] in scissors and game[1] in rock:
        return 6
    elif game[0] in rock and game[1] in paper:
        return 6
    elif game[0] in paper and game[1] in rock:
        return 0
    elif game[0] in paper and game[1] in scissors:
        return 6
    elif game[0] in scissors and game[1] in paper:
        return 0

def score(game):
    play = game[1]
    if play == "X":
        return 1
    elif play == "Y":
        return 2
    elif play == "Z":
        return 3


scores = 0
with open("input.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        game = line.split(" ")
        
        scores += check_winner(game) + score(game)

print("Total score (part 1): ", scores)


# part 2 below

def determine_new_score(line):
    if line == "A X":
        # they chose rock, we need to lose -> 0 pts
        # our choice must be scissors -> 3 pts
        return 3
        
    elif line == "A Y":
        # they chose rock, we need to draw -> 3 pts
        # our choice must be rock -> 1 pts
        return 4

    elif line == "A Z":
        # they chose rock, we need to win -> 6 pts
        # our choice must be paper -> 2 pts
        return 8
        
    elif line == "B X":
        # they chose paper, we need to lose -> 0 pts
        # our choice must be rock -> 1 pts
        return 1

    elif line == "B Y":
        # they chose paper, we need to draw -> 3 pts
        # our choice must be paper -> 2 pts
        return 5

    elif line == "B Z":
        # they chose paper, we need to win -> 6 pts
        # our choice must be scissors -> 3 pts
        return 9
        
    elif line == "C X":
        # they chose scissors, we need to lose -> 0 pts
        # our choice must be paper -> 2 pts
        return 2

    elif line == "C Y":
        # they chose scissors, we need to draw -> 3 pts
        # our choice must be scissors -> 3 pts
        return 6
        
    elif line == "C Z":
        # they chose scissors, we need to win -> 6 pts
        # our choice must be rock -> 1 pts
        return 7
        

scores = 0
with open("input.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        score = determine_new_score(line)
        scores += score


print("Total score (part 2): ", scores)
