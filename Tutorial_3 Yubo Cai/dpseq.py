"""
Yubo Cai
CSE102
Tutorial_3
"""


def fibonacci(n):
    # Initially, r0 = F_0 & r1 = F_1
    r0, r1 = 0, 1

    for _ in range(n):
        # At each iteration, assuming that r0 contains F_n and
        # r1 contains F_(n+1), we can compute F_(n+2).
        #
        # We then "slide" the window s.t. after the assignments:
        #  - r0 contains F_(n+1)
        #  - r1 contains F_(n+2)
        r0, r1 = r1, r0 + r1

        # We say that the window is of size 2 because we have two
        # variables (we could use a list of size 2 for example)

    # Starting from r0 = F_0 and r1 = F_1, after "n" iterations,
    # we know that r0 = F_n. We simply return that value.
    return r0


# Exercise 5
def next_seq(alphas, us):
    num = 0
    for i in range(len(alphas)):
        num += alphas[i] * us[i]
    return num


# Exercise 6
def u(alphas, us, n):
    if n <= len(us) - 1:
        return us[n]
    else:
        for _ in range(n):
            us = us[1:] + [next_seq(alphas, us)]
    return us[0]
