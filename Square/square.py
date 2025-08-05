def square(number):
    """Calculate the number of grains on a chessboard given a specific square.

    :param number: int - the square number (1 to 64).
    :return: int - the number of grains on the given square.
    Each square on a chessboard doubles the number of grains of rice.
    There are 64 squares on a chessboard.
    """

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    elif number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        return 2 ** (number - 1)


def total():
    """Calculate the total number of grains on a chessboard.
    :return: int - the total number of grains on the chessboard.
    There are 64 squares on a chessboard.
    """
    return 2**64 - 1
