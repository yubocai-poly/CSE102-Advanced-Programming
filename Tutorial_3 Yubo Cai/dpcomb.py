"""
Yubo Cai
CSE102
Tutorial_3
"""

import sys

sys.setrecursionlimit(10**6)

import datetime


def binom(n, k):
    if (k == 0):
        return 1
    if (k > n):
        return 0
    return binom(n - 1, k) + binom(n - 1, k - 1)


# Exercise 7

# The number of calls to binom doubles with each recursive step until
# reaching the boundary conditions, and so a rough upper bound on the
# total number of recursive calls made by binom(n,k) is O(2^n)
# (although it will be less when k is close to 0 or n).
"""
print(dt.datetime.now())
print(binom(20, 10))
print(dt.datetime.now())

2022-02-28 17:17:03.988242
184756
2022-02-28 17:17:04.075806
Time Spending: 0.097564 sec

print(dt.datetime.now())
print(binom(30, 15))
print(dt.datetime.now())

2022-02-28 17:18:23.719187
155117520
2022-02-28 17:19:41.096588
Time Spending: 1min 17.377401sec
"""


# Exercise 8
def binom_td(n, k, cache=None):
    cache = {} if cache is None else cache
    if (n, k) in cache:
        return cache[n, k]
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        cache[n, k] = binom_td(n - 1, k, cache) + binom_td(n - 1, k - 1, cache)
        return cache[n, k]


# Exercise 9
"""
starttime = datetime.datetime.now()
print(binom_td(20, 10))
endtime = datetime.datetime.now()
print(endtime - starttime)

result:
0:00:00.000172 

starttime = datetime.datetime.now()
print(binom_td(200, 100))
endtime = datetime.datetime.now()
print(endtime - starttime)

result:
0:00:00.031480
"""


# Exercise 10
def parts_td(n, k=None, cache=None):
    cache = {} if cache is None else cache
    if k is None:
        return sum(parts_td(n, k, cache) for k in range(1, n + 1))
    if (n, k) in cache:
        return cache[n, k]
    if k == 1:
        return 1
    if k > n:
        return 0
    else:
        cache[n, k] = parts_td(n - 1, k - 1, cache) + parts_td(n - k, k, cache)
        return cache[n, k]


# Exercise 11
def parts_bu(n):
    cache = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        cache[i][1] = 1
        for j in range(2, i + 1):
            cache[i][j] = cache[i - 1][j - 1] + cache[i - j][j]
    return sum(cache[n][k] for k in range(1, n + 1))


"""
starttime = datetime.datetime.now()
print(parts_td(1100))
endtime = datetime.datetime.now()
print(endtime - starttime)

result:
0:00:06.259262

starttime = datetime.datetime.now()
print(parts_bu(1100))
endtime = datetime.datetime.now()
print(endtime - starttime)

result:
0:00:01.784773
"""