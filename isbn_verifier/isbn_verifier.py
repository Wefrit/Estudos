def is_valid(isbn):
    """Verifies the validity of an ISBN-10 identifier.

    An ISBN-10 (International Standard Book Number) is a ten-digit code that uniquely
    identifies a book. The validity of an ISBN-10 is determined by a specific checksum formula.
    The checksum is calculated by multiplying each of the first nine digits by its position
    (1 through 9) and adding these products together. The tenth digit is a check digit, which
    can be a digit from 0 to 9 or the letter 'X' (representing the value 10). The sum of these
    products, plus the value of the check digit, must be divisible by 11 for the ISBN to be valid.

    Args:
        isbn (str): The ISBN-10 identifier to validate. It may contain hyphens.
        Returns:
        bool: True if the ISBN is valid, False otherwise.
    """
    isbn = isbn.replace("-", "")
    total = 0
    if len(isbn) != 10:
        return False
    for i in range(0, 10):
        if isbn[i] not in "0123456789X":
            return False
        if isbn[i].isdigit():
            total += int(isbn[i]) * (len(isbn) - i)
        elif isbn[i] == 'X':
            total += 10
    if total % 11 == 0:
        return True
    return False
