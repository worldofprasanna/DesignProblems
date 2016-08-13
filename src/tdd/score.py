def score(dice):
    def calc(n):
        if 5 == n:
            return 50
        if 1 == n:
            return 100
        return 0

    def count_and_remove(l, val):
        n = count(l, val)
        is_spl_case = (n >= 3)
        if is_spl_case:
            l = remove(l, val)
        return (is_spl_case, l)

    def count(l, val):
        return len([i for i in l if i == val])

    def remove(li, val):
        filtered_list=[i for i in li if i != val]
        val_list=[i for i in li if i == val]
        filtered_list.extend(val_list[3:])
        return filtered_list

    value = 0

    is_spl_case, dice = count_and_remove(dice, 1)
    if is_spl_case:
        value += 1000

    is_spl_case, dice = count_and_remove(dice, 5)
    if is_spl_case:
        value += 500

    for i in [2, 3, 4, 6]:
        is_spl_case, dice = count_and_remove(dice, i)
        if is_spl_case:
            value += i * 100

    if len(dice) == 0:
        return value

    for n in dice:
        value += calc(n)

    return value

