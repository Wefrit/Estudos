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
def label(colors):
    base = int(str(resistor_colors[colors[0]]) + str(resistor_colors[colors[1]]))
    
    multiplier = 10 ** resistor_colors[colors[2]]
    
    value = base * multiplier

    prefixes = [
            (1_000_000_000, "gigaohms"),
            (1_000_000, "megaohms"),
            (1_000, "kiloohms"),
            (1, "ohms")
        ]
    for divisor, suffix in prefixes:
        if value >= divisor:
            return f"{value // divisor} {suffix}"
    return "0 ohms"
