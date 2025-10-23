def primes(limit):
    is_prime = [True] * (limit +1)
    is_prime[0] = False
    is_prime[1] = False

    for n in range(2, limit+1):
        if is_prime[n]:
            for multiple in range(n*n, limit + 1, n):
                is_prime[multiple] = False
    return [n for n, prime in enumerate(is_prime) if prime]


print(primes(10))


