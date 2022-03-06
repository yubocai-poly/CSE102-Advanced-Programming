"""
Yubo Cai
CSE102
Tutorial_3
"""


# Exercise 1
def catalan(n):
    if n < 0:
        pass
    if n == 0:
        return 1
    num = 0
    for i in range(0, n):
        num += catalan(i) * catalan(n - i - 1)
    return num


# Exercise 2
def catalan_td(n, cache=None):
    cache = {} if cache is None else cache
    if n not in cache:
        # This is the first time we compute `catalan(n)`
        # Compute it and store the result in `cache[n]`
        if n <= 0:
            cache[n] = 1
        else:
            cache[n] = sum(
                catalan_td(i, cache) * catalan_td(n - 1 - i, cache)
                for i in range(0, n))
    # At that point, we know that `cache[n]` exists and
    # is exactly the n-th Catalan number
    # We simply return it.
    return cache[n]


# Exercise 3
def next_catalan(cs):
    n = len(cs)
    if cs == []:
        return 1
    else:
        return sum(cs[i] * cs[n - i - 1] for i in range(0, n))


# Exercise 4
def catalan_bu(n):
    if n <= 0:
        return 1
    lis = []
    for _ in range(n + 1):
        lis.append(next_catalan(lis))
    return lis[-1]