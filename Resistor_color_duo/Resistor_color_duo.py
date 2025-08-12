resistor_colors = {"black": 0,
"brown": 1,
"red": 2,
"orange": 3,
"yellow": 4,
"green": 5,
"blue": 6,
"violet": 7,
"grey": 8,
"white": 9}
def value(colors):
    """Returns the numeric value of a resistor based on its color bands.

    Args:
        colors (list): A list of two strings representing the colors of the resistor bands.
    Returns:
        int: The numeric value corresponding to the two color bands.
    """
    number = ''
    for color in colors:
        number += str(resistor_colors[color])
    int_number = int(number)
    return int_number


print(value(['orange', 'orange']))  # Output: 33 


