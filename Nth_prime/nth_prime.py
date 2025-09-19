def prime(number):
    primes = []
    while len(primes) < number:
        for n in range (1, number + 1):
            if n == 2:
                primes.append(n)
            else:
                for number in primes:
                    if n % number != 0:
                        primes.append(n)
                    else:
                        continue
    return primes

print(prime(6))