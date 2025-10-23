def triplets_with_sum(number):
    triplets = []
    for a in range(1, number + 1):
        for b in range(a + 1, number):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer():
                c = int(c)
                if a + b + c == number:
                    triplets.append((a, b, c))
    return triplets

print(triplets_with_sum(1000))