"""
The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

"""

import nose.tools as test


def convert(rgb):
    if rgb <= 0:
        return '00'
    elif rgb > 255:
        return 'FF'
    else:
        hex_numb = hex(rgb).replace('x', '').upper()
        if len(hex_numb) > 2:
            hex_numb = hex_numb[1:]
        return hex_numb


def rgb(r, g, b):
    return '{}{}{}'.format(convert(r), convert(g), convert(b))


test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")
