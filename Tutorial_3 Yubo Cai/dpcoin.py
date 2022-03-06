"""
Yubo Cai
CSE102
Tutorial_3
"""

import math as math

import sys

sys.setrecursionlimit(10**6)

CURRENCY = [1, 3, 7, 9]

# credit to Junyuan Wang


def transacts_num(n, cache=None):

    cache = {} if cache is None else cache
    if n == 0:
        return 0
    if n in CURRENCY:
        return 1

    l = []
    for c in CURRENCY:
        if n < c:
            continue
        if n - c in cache:
            l.append(1 + cache[n - c])
        else:
            cache[n - c] = transacts_num(n - c, cache)
            l.append(1 + cache[n - c])

    return min(l)