"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a
single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

"""


def find_outlier(integers):
    odd = []
    even = []
    for numb in integers:
        if numb % 2 == 0:
            odd.append(numb)
        else:
            even.append(numb)
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]


assert find_outlier([2, 4, 6, 8, 10, 3]) == 3
assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160
