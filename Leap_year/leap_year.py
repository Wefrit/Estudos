def leap_year(year):
    """
    Determine if a given year is a leap year.
    :param year: int - the year to check.
    :return: bool - True if the year is a leap year, False otherwise.
    A year is a leap year if:
    - It is divisible by 4;
    - If it is divisible by 100, it must also be divisible by 400.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
    return False

print(leap_year(2100)) 