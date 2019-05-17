from __future__ import division
import sys

def fact(n):
    """
    Factorial function
    :arg n: Number
    :returns: factorial of n
    """
    if n == 0:
        return 1
    return n * fact(n - 1)


def div(n):
    """
	  Simple Divide Function
	  """
    result = 33 / n
    return round(result, 2)


def stest_sum(n):
    """
	  It takes an iterable and adds the values together
	  """
    total = 0
    for val in n:
        total += val
    return total


def main(n, y):
    res = fact(n)
    print(res)
    res1 = div(y)
    print(res1)
    res2 = stest_sum([n, y])
    print(res2)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]), int(sys.argv[2]))
