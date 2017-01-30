from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative(skip_after_fail=True):
    with tested_function_name("is_prime"), all_or_nothing():
        is_prime = reftest()

        for i in range(0,100):
            is_prime(i)

    with tested_function_name("count_primes_below"), all_or_nothing():
        count_primes_below = reftest()

        for i in range(0,100):
            count_primes_below(i)

    with tested_function_name("gcd"), all_or_nothing():
        gcd = reftest()

        quicktest(0, 0, 0)
        quicktest(5, 0, 5)
        quicktest(5, 20, 5)
        quicktest(13, 13 * 5, 13 * 7)
        quicktest(7, -7 * 5, -7 * 4)
        quicktest(7, -7 * 5, 7 * 4)
        quicktest(7, 7 * 5, -7 * 4)

        for i in [-1500, -80, -17, 0, 16, 41, 5000]:
            for j in [-2000, -10, -3, 0, 16, 59, 4000]:
                gcd(i, j)
