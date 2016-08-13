def score(dice):
    def calc(n):
        if 5 == n:
            return 50
        if 1 == n:
            return 100

    value = 0
    if len(dice) == 0:
        return value

    for n in dice:
        value += calc(n)

    return value

