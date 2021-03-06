"""

You will be given an array which lists the current inventory of stock in your store and another array which lists the new inventory being delivered
to your store today.

Your task is to write a function that returns the updated list of your current inventory in alphabetical order.

"""


def update_inventory(cur_stock, new_stock):
    cur_stock = cur_stock + new_stock
    results = {}
    for cur in cur_stock:
        if cur[-1] not in results.keys():
            results[cur[1]] = cur[0]
        else:
            results[cur[1]] += cur[0]
    results = [(i[1], i[0]) for i in results.items()]
    results.sort(key=lambda x: x[1])
    return results


current = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
new = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]
result = [(15, 'Apple'), (25, 'HTC'), (5, 'LG'), (1000, 'Nokia'), (54, 'Samsung'), (43, 'Sony')]
assert update_inventory(current, new) == result
