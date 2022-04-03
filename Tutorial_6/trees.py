"""
Yubo Cai
CSE102
Tutorial_6
2022.03.28
"""

import math


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


T1 = Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5)))
T2 = Node(0, Node(1), Node(2, Node(3), Node(4, Node(5))))
T3 = Node(11, Node(10, Node(9, None, Node(8)), Node(7)), Node(6))
T4 = Node(0, Node(2, Node(4, None, Node(5)), Node(3)), Node(1))
T5 = Node(0, Node(2, Node(2)))


# Exercise 1 计算node节点的数量
def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)


print(size(T1))
print(size(T2))
print(size(T3))


# Exercise 2 计算tree上所有node的值
def sum_values(root):
    if root is None:
        return 0
    return root.value + sum_values(root.left) + sum_values(root.right)


print(sum_values(T1))
print(sum_values(T2))
print(sum_values(T3))


# Exercise 3 计算tree的高度
def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))


print(height(T1))
print(height(T2))
print(height(T3))


# Exercise 4 计算是否是mirror tree
def mirrored(lroot, rroot):
    if sum_values(lroot) != sum_values(rroot):
        return False
    if size(lroot) != size(rroot):
        return False
    if height(lroot) != height(rroot):
        return False

    cnull = (lroot is None) + (rroot is None)

    if cnull > 0:
        # If at least 1 of the parameters if `None`, then `lnode` is a
        # mirror of `rnode` iff both are empty (i.e. equal to `None`)
        return cnull == 2

    # Otherwise, both are non empty. We just check that they have the
    # same root value and that their left-right and right-left
    # children are mirror trees.

    if ((lroot.value == rroot.value) and mirrored(lroot.left, rroot.right)
            and mirrored(lroot.right, rroot.left)):
        return True
    else:
        return False


print(mirrored(T2, T4))
print(mirrored(T1, T3))
print(mirrored(T1, T1))


# Exercise 5 计算自己是否自身·对称
def check_symmetry(root):
    return mirrored(root, root)


T5 = Node(0, Node(2, Node(3, None, None), None),
          Node(2, Node(3, None, None), None))
print(check_symmetry(T5))


# Exercise 8 检查这个tree是不是二叉树
def check_BST(root, lmin=-math.inf, lmax=math.inf):
    if root is None:
        # The empty tree is a BST and validate the extra restrictions.
        return True
    if (lmin <= root.value <= lmax) and check_BST(
            root.left, lmin, root.value) and check_BST(root.right, root.value,
                                                       lmax):
        return True
    else:
        return False


T6 = Node(0, Node(-1, Node(-2, None, None), Node(-3, None, None)), None)
print(check_BST(T6))


# Exercise 9 返回根部的最小值
def min_BST(root):
    if root is None:
        return math.inf
    if root.left is None:
        return root.value
    return min_BST(root.left)

# 因为在BST中左侧的肯定比右侧小
