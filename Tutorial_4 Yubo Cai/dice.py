"""
Yubo Cai
CSE102
Tutorial_4
"""


# Exercise 3
def slice_dice(n, s, dice):
    return [dice[i * s:i * s + s] for i in range(n)]


# Exercise 4
def win_probability(die1, die2):

    n = len(die1)
    case = 0

    for d1 in die1:
        for d2 in die2:
            if d1 > d2:
                case += 1

    return case / (n * n)


print(win_probability([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]))
print(win_probability([1, 2, 3, 4], [3, 4, 5, 6]))


def beats(die1, die2):
    return win_probability(die1, die2) > 0.5


# Exercise 5
def get_dice(n, s, dice):
    """Find by backtracking search n cyclic dice with s sides.

    a partial solution of size k is already given in dice
    """
    k = len(dice)
    if k == n * s:
        if beats(dice[-s:], dice[:s]):
            yield dice
        else:
            return
    else:
        for i in range(n * s):
            # already used
            if i in dice:
                continue
            # not the first element of a die, but not increasing
            if k % s != 0 and i <= dice[-1]:
                continue
            newd = dice + [i]
            # finished a die, and already more than two dice but not A>B
            if (
                k % s == s - 1
                and k + 1 >= 2 * s
                and not beats(newd[-2 * s : -s], newd[-s:])
            ):
                continue
            yield from get_dice(n, s, newd)
