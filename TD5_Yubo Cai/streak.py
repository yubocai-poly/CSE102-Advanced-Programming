"""
Yubo Cai
CSE102
Tutorial_5
"""
import random


# Exercise 1
def experiment1(N, k):
    count = 0
    for i in range(N):
        if random.choice([True, False]) is True:
            count += 1
            if count >= k:
                return True
        else:
            count = 0
    return False


def experiment(N, k):
    num = 100000
    t = 0
    for i in range(num):
        if experiment1(N, k) is True:
            t += 1
    return t / num

print(experiment(10, 4))
