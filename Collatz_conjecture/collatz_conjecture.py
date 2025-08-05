def steps(number):
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

print(steps(12))