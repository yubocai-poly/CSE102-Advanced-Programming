"""
Yubo Cai
CSE102
Tutorial_6
2022.04.04
"""


# Exercise 1
def matrix_to_adjlist(M):
    n = len(M)
    L = []
    for i in range(n):
        L.append([])
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                L[i].append(j)
    return L
    


def _main_mtrx_to_list():
    M = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    mat1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    mat2 = [[0, 0, 0, 0, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0]]
    print(matrix_to_adjlist(M))
    print(matrix_to_adjlist(mat1))
    print(matrix_to_adjlist(mat2))


# Exercise 2
def edges(G):
    for i, s in enumerate(G):
        yield from [(i, j) for j in s]

def is_symmetric(G):
    for u, v in edges(G):
        if not u in G[v]:
            return False
    return True

def _main_is_symmetric():
    G = [[1], [2], [0]]
    print(is_symmetric(G))
    G = [[1], [0], []]
    print(is_symmetric(G))


# Exercise 3
G = [[1], [2], [0]]
test1 = [[], [], []]
test2 = [[], [2, 0], [], [], [0, 3]]

def revert_edges(G):
    sub_G = [[] for _ in range(len(G))]
    
    for u, v in edges(G):
        sub_G[v].append(u)
    return sub_G

print(revert_edges(G))
print(revert_edges(test1))
print(revert_edges(test2))
    


    


