def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = tuple(x for x in range(2, 51) if is_prime(x))

print(primes)
