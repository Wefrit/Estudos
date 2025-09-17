def factors(value):
    div = 2
    factor = []
    while value > 1:
        if value % div == 0:
            value /= div
            factor.append(div)
            print(value)
        else:
            div += 1
    return factor
