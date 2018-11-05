
"""

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

"""

from functools import reduce
from operator import mul
import nose.tools as test



def factorial(n):
    return reduce(mul, range(1, (n + 1)), 1)


def zeros(n):
    fact = str(factorial(n))[::-1]
    zeros_count = 0
    for char in fact:
        if char != '0':
            break
        zeros_count += 1
    return zeros_count


test.assert_equals(zeros(0), 0, "Testing with n = 0")
test.assert_equals(zeros(6), 1, "Testing with n = 6")
test.assert_equals(zeros(30), 7, "Testing with n = 30")
