"""
Yubo Cai
CSE102
Tutorial_8
2022.04.18
"""


# Exercise 6
def tap_uint16(x, i):
    """ Return 1 or 0 depending on whether the ith-least significant bit
        of x is 1 or 0.
    """
    return (x >> i) & 1


# Exercise 7
def polytap_uint16(x, I):
    """ Tap x at all the positions in I (which is a list of tap
        positions) and return the xor of all of these tapped values.
    """
    result = 0
    for i in I:
        result ^= tap_uint16(x, i)
    return result


# Exercise 8
def lfsr_uint16(x, I):
    """Return the successor of x in an LFSR based on tap positions I"""
    return (x >> 1) | (polytap_uint16(x, I) << 15)


def test_lfsr_uint16(seed):
    I = [0, 2, 3, 5, 15]
    xs = [seed]
    for _ in range(10):
        xs.append(lfsr_uint16(xs[-1], I))
    return xs

assert test_lfsr_uint16(42) == [42, 21, 10, 32773, 49154,
                                57345, 28672, 14336, 7168,
                                3584, 1792]