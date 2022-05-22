"""
Yubo Cai
CSE102
Tutorial_6
2022.04.04
"""
import math


def shortest_route_len(G, s, t):
    q = [s]
    distance = []
    for i in range(len(G)):
        if i == s:
            distance.append(0)
        else:
            distance.append(math.inf)
    while q is not None:
        c = q.pop(0)
        if c == t:
            return distance[t]
        for ele in G[c]:
            if distance[ele] == math.inf:
                distance[ele] = distance[c] + 1
                q.append(ele)
    return math.inf
