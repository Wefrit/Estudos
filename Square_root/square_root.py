def square_root(number):
    """Compute the square root of a given number.

    Args:
        number: The number to compute the square root of. Must be non-negative.

    Returns:
        int: The square root of the given number.
    """
    list = []
    while number > 1:
        for n in range(2, number + 1):
            if number % n == 0:
                number //= n
                list.append(n)
                break
    for item in range(len(list)-1,-1,-1):
        if item % 2 == 0:
            list.pop(item)
    root = 1
    for n in list:
        root *= n
    return root

print(square_root(676))