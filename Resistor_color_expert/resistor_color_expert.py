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

resistor_tolerance = {"grey": "±0.05%",
"violet": "±0.1%",
"blue": "±0.25%",
"green": "±0.5%",
"brown": "±1%",
"red": "±2%",
"gold": "±5%",
"silver": "±10%"}

def resistor_label(colors):
    """Returns the label of a resistor based on its color bands.

    Args:
        colors (list): A list of three strings representing the colors of the resistor bands.
    Returns:
        str: The label of the resistor in ohms, kiloohms, megaohms, or gigaohms and it's tolerance.    
    """

    if len(colors) == 5:
        base = int(
            str(resistor_colors[colors[0]]) + 
            str(resistor_colors[colors[1]]) + 
            str(resistor_colors[colors[2]])
        )
        multiplier = 10 ** resistor_colors[colors[3]]
        value = base * multiplier
        tolerance = resistor_tolerance[colors[4]]

    elif len(colors) == 4:
        base = int(str(resistor_colors[colors[0]]) + str(resistor_colors[colors[1]]))
        multiplier = 10 ** resistor_colors[colors[2]]
        value = base * multiplier
        tolerance = resistor_tolerance[colors[3]]
        
    else:
        return "0 ohms"

    prefixes = [
        (1_000_000_000, "gigaohms"),
        (1_000_000, "megaohms"),
        (1_000, "kiloohms"),
        (1, "ohms")
    ]
    for divisor, suffix in prefixes:
        if value >= divisor:
            return f"{value / divisor:.0f} {suffix} {tolerance}"


print(resistor_label(["blue", "grey", "brown", "violet"]))  # Example usage