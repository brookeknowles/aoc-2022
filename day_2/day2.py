
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

print("Total score: ", scores)