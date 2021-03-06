"""

Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency in cents, and returns a dictionary which shows the least
amount of coins used to make up that amount. The only coin denominations considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). Therefor the dictionary returned should contain exactly 4 key/value pairs.

loose_change(56)  ->  {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}
A couple notes regarding expected behavior:

• If the function is passed either 0 or a negative number, the function should return the dictionary with all values equal to 0.

loose_change(-435)  ->  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
• If a float is passed into the function, its value should be be rounded down, and the resulting dictionary should never contain fractions of a coin.

loose_change(4.935)  ->  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}

"""

import nose.tools as test


def loose_change(cents):
    change_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents <= 0:
        return change_dict
    cents, count = calc(cents, 25)
    change_dict['Quarters'] += count
    cents, count = calc(cents, 10)
    change_dict['Dimes'] += count
    cents, count = calc(cents, 5)
    change_dict['Nickels'] += count
    cents, count = calc(cents, 1)
    change_dict['Pennies'] += count
    return change_dict


def calc(cents, coin):
    count = 0
    while cents >= coin:
        cents -= coin
        count += 1
    return cents, count


test.assert_equals(loose_change(29), {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1})
test.assert_equals(loose_change(91), {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3})
test.assert_equals(loose_change(0), {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(-2), {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})
