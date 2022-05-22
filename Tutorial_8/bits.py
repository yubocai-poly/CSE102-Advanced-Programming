"""
Yubo Cai
CSE102
Tutorial_8
2022.04.18
"""


# Exercise 1
def reverse_lis(lis):
    # 反转列表
    lis.reverse()
    return lis


def uint16_to_bitstring(x):
    # 十进制转化二进制, 用 16 位表示
    lis = []
    if x <= 0:
        return [0] * 16

    if x > 2**16 - 1:
        return [1] * 16

    while x > 0:
        bit = x % 2
        x = x // 2
        lis.append(bit)

    # 高位补零，穿插0进去
    for i in range(16 - len(lis)):
        lis.append(0)

    return reverse_lis(lis)


print(uint16_to_bitstring(0))
print(uint16_to_bitstring(42))
print(uint16_to_bitstring(255))


# Exercise 2
def bitstring_to_uint16(bs):
    # 将二进制转化为十进制
    num = 0

    if len(bs) != 16:
        return -1

    for i in range(16):
        num += bs[i] * 2**(15 - i)

    return num


print(bitstring_to_uint16([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(bitstring_to_uint16([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]))
print(bitstring_to_uint16([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]))

assert (42 == bitstring_to_uint16(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]))

# check that all 16 bit numbers survive a roundtrip through bitstrings
# 程序检查代码是否能够正确转换为二进制，并且能够转换回来
for n in range(1 << 16):
    bs = uint16_to_bitstring(n)
    nn = bitstring_to_uint16(bs)
    if nn != n:
        print(
            'Oops! Error found with the following number, to_bitstring, and to_int: ',
            n, bs, nn)
    break


# Exercise 3
def mod_pow2(x, k):
    # 计算 x^k mod 2^k 只能够使用二进制的方法
    # 计算最大的 2^k - 1， 最大的 2^k - 1 可以用二进制表示为 111...1
    a = (1 << k) - 1
    return x & a


# Exercise 4
def is_pow2(x):
    if n < 0:
        return False

    # 判断 x 是否是 2 的幂
    return (x > 0) and (x & (x - 1) == 0)


print(is_pow2(0))
print(is_pow2(4))
print(is_pow2(42))


# Exercise 5
def set_mask(w, m):
    """set every bit position which is 1 in m, to 1 in w"""
    return w | m


def toggle_mask(w, m):
    """toggle every bit position which is 1 in m, in w"""
    return w ^ m


def clear_mask(w, m):
    """set every bit position which is 1 in m, to 0 in w"""
    return w & ~m
