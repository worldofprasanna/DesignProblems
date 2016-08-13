def score(dice):
    def calc(n):
        if 5 == n:
            return 50
        if 1 == n:
            return 100
        return 0

    def count(l, val):
        return len([i for i in l if i == val])

    def remove(li, val):
        filtered_list=[i for i in li if i != val]
        val_list=[i for i in li if i == val]
        filtered_list.extend(val_list[3:])
        return filtered_list

    value = 0

    if count(dice, 1) >= 3:
        dice = remove(dice, 1)
        value += 1000

    if count(dice, 5) >= 3:
        dice = remove(dice, 5)
        value += 500

    for i in [2, 3, 4, 6]:
        if count(dice, i) >= 3:
            dice = remove(dice, i)
            value += i * 100

    if len(dice) == 0:
        return value

    for n in dice:
        value += calc(n)

    return value

