"""
Yubo Cai
CSE102
Tutorial_4
"""


# Exercise 1
def subseq(seq):
    if seq == []:
        yield seq
    else:
        for sub in subseq(seq[1:]):
            yield sub
            yield [seq[0]] + sub
            
for i in subseq([1,2,3]):
    print(i)
