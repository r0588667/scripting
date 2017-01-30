def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return n > 1


def count_primes_below(n):
    count = 0

    for i in range(0, n):
        if is_prime(i):
            count += 1

    return count


def gcd(x, y):
    x = abs(x)
    y = abs(y)

    for i in range(max(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i

    return 0