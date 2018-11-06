"""
Write a function that returns the degree of a polynomial function:

degree(x => 42);                    // 0
degree(x => x);                     // 1
degree(x => x * x);                 // 2
degree(x => x * x * x);             // 3
degree(x => 2 * x + 3 * x * x + 5); // 2
Assume that the polynomial has a maximum degree of 11
The input x of the polynomial function
must be between -11 and 11
use integers to get exact results without rounding errors

"""

import nose.tools as test


def degree(p):
    count = 0
    base = 2
    result = p(base)
    print(result, base * base * base)

    tmp = base
    while True:
        if tmp > result:
            return 0
        if tmp == result:
            return count + 1
        tmp = tmp * base
        count += 1


test.assert_equals(degree(lambda x: 42), 0)

test.assert_equals(degree(lambda x: x), 1)

test.assert_equals(degree(lambda x: x * x), 2)

test.assert_equals(degree(lambda x: x * x * x), 3)

test.assert_equals(degree(lambda x: x * x * x * x), 4)

test.assert_equals(degree(lambda x: x * x * x * x * x), 5)

test.assert_equals(degree(lambda x: 5 + 3 * x + 2 * x * x), 2)
