def prime(number):
    primes = []
    n = 2
    if number < 1:
        raise ValueError('there is no zeroth prime')
    while len(primes) < number:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
        n += 1
    return primes[-1]
                        

