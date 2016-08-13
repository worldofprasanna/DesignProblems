def score(dice):
    value = 0
    if len(dice) == 0:
        return value

    if 5 == dice[0]:
        return 50
    if 1 == dice[0]:
        return 100

