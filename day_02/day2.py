# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

data = open("./input.txt").read().split('\n')

def isWin(c1, c2):
    if c2 == 'X' and c1 == 'C':
        return True
    elif c2 == 'Y' and c1 == 'A':
        return True
    elif c2 == 'Z' and c1 == 'B':
        return True
    return False

def isDraw(c1, c2):
    if c1 == 'A' and c2 == 'X':
        return True
    elif c1 == 'B' and c2 == 'Y':
        return True
    elif c1 == 'C' and c2 == 'Z':
        return True
    return False

def appendScore(c2):
    if c2 == 'X':
        return 1
    elif c2 == 'Y':
        return 2
    elif c2 == 'Z':
        return 3

score1 = 0

# Start of the code and add score 
for str in data:
    c1 = str[0]
    c2 = str[2]
    score1 += appendScore(c2)
    if isWin(c1, c2):
        score1 += 6
    elif isDraw(c1, c2):
        score1 += 3
    
print(score1)
# check if won / lose / draw and add scores




