from random import randint

def playOneGame():
    rollResult = randint(1, 6) + randint(1, 6)
    if rollResult == 7 or rollResult == 11:
        return 1
    if rollResult == 2 or rollResult == 3 or rollResult == 12:
        return -1
    else:
        count = 2
        rollResult2 = randint(1, 6) + randint(1, 6)
        while rollResult2 != rollResult and rollResult2 != 7:
            count += 1
            rollResult2 = randint(1, 6) + randint(1, 6)
        if rollResult2 != rollResult:
            return count
        else:
            return (-1)*count
    return

print(playOneGame())
