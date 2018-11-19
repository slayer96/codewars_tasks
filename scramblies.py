"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""

import nose.tools as test


# def scramble(s1, s2):
#     s1 = list(s1)
#     s2 = list(s2)
#     s1.sort()
#     s2.sort()
#     g1 = gen(s1)
#     g2 = gen(s2)
#     c2 = next(g2)
#     while True:
#         c1 = next(g1)
#         if c1 == c2:
#             try:
#                 c2 = next(g2)
#             except StopIteration:
#                 return True
#             continue
#         if c2 < c1:
#             return False
#
#
# def gen(s):
#     for i in s:
#         yield i

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


test.assert_equals(scramble('rkqodlw', 'world'),  True)
test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
test.assert_equals(scramble('katas', 'steak'), False)
test.assert_equals(scramble('scriptjava', 'javascript'), True)
test.assert_equals(scramble('scriptingjava', 'javascript'), True)
