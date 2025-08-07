def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    types = ["perfect", "deficient", "abundant"]
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    divisors = sum(n for n in range(1, number) if number % n == 0)
    return types[0] if divisors == number else types[1] if divisors < number else types[2]
