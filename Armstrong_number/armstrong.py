def is_armstrong_number(number):
    """
    Check if a number is an Armstrong number.
    An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits
      each raised to the power of the number of digits.
    """
    digits = str(number)
    sum_of_digits = 0
    for digit in digits:
        digit_power = int(digit) ** len(digits)
        sum_of_digits += digit_power
    return sum_of_digits == number
