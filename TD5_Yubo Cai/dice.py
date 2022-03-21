"""
Yubo Cai
CSE102
Tutorial_5
"""
import random


# Exercise 3
def roll(D):
    total = [D[0]]
    k = len(D)
    for i in range(1, k):
        total.append(D[i] + total[i - 1])

    x = random.random()

    for i in range(k):
        if total[i] > x:
            return i + 1


# 按照d的概率随机构建一个筛子，然后给面编号，摇到哪个就是返回哪个相对应的数字
# 构造的total数列每一个间距，就是两个相邻的差是这个面的概率


# Exercise 4
def rolls(D, N):
    l = []
    for _ in range(N):
        l.append(roll(D))

    result = [0] * len(D)
    for ele in l:
        result[ele - 1] += 1

    return result


"""
掷骰子N次，然后返回一个list，这个list出现按照对应概率的每个面出现的次数
rolls([1/6,1/3,1/2],10)
[3, 2, 5]
3,2,5分别对应1/6, 1/3, 1/2出现的概率
"""

# Exercise 5
import matplotlib.pyplot as plt


def plot(ns):
    N = sum(ns)
    ns = [float(x) / N for x in ns]
    plt.bar(range(len(ns)), height=ns)
    plt.xticks(range(len(ns)), [str(i + 1) for i in range(len(ns))])
    plt.ylabel('Probability')
    plt.title('Biased die sampling')
    plt.show()


plot(rolls([1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6], 10000))
