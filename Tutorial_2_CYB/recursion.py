#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:38:27 2022

@author: Yubo Cai
"""


# Question 1
# --------------------------------------------------------------------
def binom(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return binom(n - 1, k) + binom(n - 1, k - 1)


# Question 2
# --------------------------------------------------------------------
def choose(S, k):
    if k == 0:
        return [[]]
    if k > len(S):
        return []

    l = []
    for el in choose(S[1:], k - 1):
        l.append([S[0]] + el)
    return l + choose(S[1:], k)


# Question 3
# --------------------------------------------------------------------
def permutations(L):
    if len(L) == 0:
        return [L]
    lis = []
    for p in permutations(L[1:]):
        for i in range(len(L)):
            lis.append(p[0:i] + [L[0]] + p[i:])

    return lis

# Question 4
# --------------------------------------------------------------------
def choose_not_recursion(S, k):
    if k == 0:
        return [[]]
    if k > len(S):
        return []

    

# Question 6
# --------------------------------------------------------------------
def not_angry(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    else:
        return not_angry(n - 1) + not_angry(n - 2)
"""
By computation
n = 2 have 3 possibilities
n = 3 have 5 possibilities
n = 4 have 8 possibilities
n = 5 have 13 possibilities
Then I find this sequence is Fibonacci sequence
"""
