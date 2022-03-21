"""
Yubo Cai
CSE102
Tutorial_5
"""
import random


# Exercise 2
def penny():
    lis = []
    while True:
        lis.append(random.choice([True, False]))
        if len(lis) > 3:
            lis.pop(0)
        if lis == [True, True, False]:
            return True
        if lis == [False, True, True]:
            return False


def experiment():
    num = 100000
    c = 0
    for i in range(num):
        if penny() is True:
            c += 1

    return c / num


print(experiment())