def rgb_to_hex(red, green, blue):
    red_hex = hex(red)[2:].zfill(2)
    green_hex = hex(green)[2:].zfill(2)
    blue_hex = hex(blue)[2:].zfill(2)
    if red > 255 or green > 255 or blue > 255:
        return 'FFFFFF'
    return red_hex + green_hex + blue_hex






# The hex function is a built-in Python function that converts an integer to its hexadecimal representation. 
# When hex(blue) is called, the function returns a string that starts with the characters '0x' 
# followed by the hexadecimal representation of the blue value. 
# For example, if blue is equal to 11, hex(blue) would return the string '0xb'.

# The [2:] part of the code is used to remove the first two characters ('0x') from the hexadecimal string returned by hex(blue). 
# This is because we only want the hexadecimal representation of the blue value, without the '0x' prefix.

# The zfill(2) method is then called on the resulting string to ensure that the hexadecimal representation 
# is always two characters long. If the string is already two characters long, zfill(2) has no effect. 
# If the string is shorter than two characters, zfill(2) pads the string with '0' characters on the left 
# until it is two characters long.



# If any of the input values is greater than 255, the function should return 'FFFFFF', which represents white. 
# We can fix this by checking if any value is greater than 255 and returning 'FFFFFF' in that case.

def test_rgb_solution():
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'
    assert rgb_to_hex(255, 255, 300) == 'FFFFFF'
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(148, 0, 211) == '9400D3'
    assert rgb_to_hex(254,253,252) == "FEFDFC"
    assert rgb_to_hex(220, 67, 368) == "DC43FF"



# The first two assertions will fail, as the input values (255, 255, 300) are invalid. 
# The third assertion will pass, as the input values (0, 0, 0) represent black. 
# The fourth assertion will pass, as the input values (148, 0, 211) represent a shade of purple. 
# The fifth assertion will pass, as the input values (254, 253, 252) represent an off-white color. 
# The sixth assertion will fail, as the input values (220, 67, 368) are invalid.