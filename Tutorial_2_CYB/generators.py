#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:38:27 2022

@author: Yubo Cai
"""


# Question 9
# --------------------------------------------------------------------
def fibs():
    index, a, b = 0, 0, 1
    while True:
        yield a
        a, b = b, a + b
        index = index + 1


# Question 10
# --------------------------------------------------------------------
def prefix_sums(k):
    sum = k
    while True:
        yield sum
        k += 1
        sum += k


# Question 12
# --------------------------------------------------------------------
def choose_gen(S, k):
    if k == 0:
        yield []
        return 

    if k > len(S):
        return 

    for el in choose_gen(S[1:], k - 1):
        yield [S[0]] + el
    for el in choose_gen(S[1:], k):
        yield el