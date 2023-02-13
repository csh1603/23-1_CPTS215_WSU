import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return True
    return False

def sum_primes(M):
    sum = 0
    res = False
    for j in range(2, M+1):
        res = is_prime(j)
        if res == False:
            sum += j
    return sum

n = int(input("Please enter an integer >= 2:"))
if n >= 2:
    out = is_prime(n)
    if out is True:
        print("{0} is not prime!".format(n))
    else:
        print("{0} is prime!".format(n))

    print("Sum of primes from 2 to {0} is {1}!".format(n, sum_primes(n)))