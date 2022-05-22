"""
Yubo Cai
CSE102
Tutorial 10
2022.05.16
"""

################################################ Validating user input ################################################


class InvalidInput(Exception):
    pass


class Found(Exception):

    def __init__(self, solution):
        self.solution = solution

# Exercise 1
def sum_of_input():
    s = 0
    while True:
        try:
            n = int(input("Enter a number: "))

            s += int(n)
        except EOFError:
            return s
        except:
            raise InvalidInput



################################################ Revisiting backtracking ################################################


# Exercise 2
def subset_sum(nm, S, M):
    # "nm" is the set of available numbers
    # "M" is the target sum
    # "S" is the current partial solution
    nS = sum(S)  # The sum of the partial solution

    if nS > M:
        # "S" is a non-feasible solution.
        # We reject it.
        return None

    if nS == M:
        # S is a valid solution.
        # We accept it.
        raise Found(S)
    for i in nm:
        # Otherwise, we try to extend S with the integers
        # from "nm" - 1 by 1 and continue recursively.
        rS = subset_sum(
            nm.difference([i]),  # We remove "i" from "nm"
            S.union([i]),  # We add "i" to "S"
            M  # The targeted sum is unchanged
        )

        if rS is not None:
            # We found a solution (recursively)
            # We return it
            return rS

    # We tried all the numbers in "nm" without finding
    # a solution. We report the failure with "None"
    return None