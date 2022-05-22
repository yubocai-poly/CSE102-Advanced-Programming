"""
Yubo Cai
CSE102
Tutorial_6
2022.04.04
"""

# Exercise 4
"""
General setup: a university’s curriculum consists of courses (numbered from 0 to n). 
Each course has prerequisites (other courses that should be passed before enrolling into the course). 
In the problems below, you will be given a graph G of courses (with edges from a course to all its prerequisites)
represented via adjacency list.
"""


def required(G, c, visited=None):
    """
    Write a function required(G, c) that takes a course number c 
    and returns the number of courses that have to be passed in order to pass c (including c itself).
    
    For example, required([[1], [2, 3], [], [2], [2]], 1) should return 3.
    """
    visited = set() if visited is None else visited
    # we apply the set in order to avoid duplicates

    # then we can apply teh the DFS
    if c not in visited:
        visited.add(c)
        for v in G[c]:
            required(G, v, visited)
            print(visited)

    return len(visited)


# Exercise 5
def required_list(G, c, visited=None):
    lis = []
    visited = set() if visited is None else visited
    # we apply the set in order to avoid duplicates

    # then we can apply teh the DFS
    if c not in visited:
        visited.add(c)
        for v in G[c]:
            required(G, v, visited)

    for el in visited:
        lis.append(el)

    return lis


# Exercise 7


def edges(G):
    for i, s in enumerate(G):
        yield from [(i, j) for j in s]


def revert_edges(G):
    sub_G = [[] for _ in range(len(G))]

    for u, v in edges(G):
        sub_G[v].append(u)
    return sub_G


def needed_for(G, c):
    inverse_lis = revert_edges(G)
    return required(inverse_lis, c)