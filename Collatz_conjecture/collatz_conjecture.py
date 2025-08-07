def steps(number):
    """
    Calculate the number of steps required to reach 1 in the Collatz conjecture sequence.
    The Collatz conjecture is defined as follows:
    - If the number is even, divide it by 2.
    - If the number is odd, multiply it by 3 and add 1.
    The process is repeated until the number reaches 1.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    number_of_steps = 0
    num = number
    while num != 1:
        if num % 2 != 0:
            num  = (num * 3) + 1
            number_of_steps += 1
        else:
            num = num // 2
            number_of_steps += 1
    return number_of_steps   
