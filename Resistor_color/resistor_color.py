codes ={"black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9}
def color_code(color):
    """Returns the numeric value of a resistor color code.

    Args:
        color (str): The color of the resistor band.
    Returns:
        int: The numeric value corresponding to the color. 
    """
    return codes[color]


def colors():
    """
    Returns:
        list: A list of strings representing the colors of the resistor bands.
    """
    return list(codes.keys())

print(color_code("red"))  # Output: 2
print(colors())  # Output: ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']