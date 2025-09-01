def sum_of_multiples(limit, multiples):
    """Given a limit and a list of multiples, return the sum of all unique multiples
    of the multiples up to but not including the limit.
    If a number is a multiple of more than one base, count it only once.
    For instance, if the limit is 20 and the multiples are 3 and 5, the multiples
    would be 3, 5, 6, 9, 10, 12, 15, and 18 for a total of 78.
    """

    uniques = set()
    for n in range(1, limit):
        for multiple in multiples:
            if multiple > 0 and n % multiple == 0:
                uniques.add(n)
    return sum(item for item in uniques )
