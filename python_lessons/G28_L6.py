# Group 28 (u23531003, u23551195, u23575035, u23618117, u23664542)

'''
Objective: Teach learners how to find the best way of solving a problem.
Action: Provide different ways of doing the same function, while ranking them in effectiveness. (e.g. 1st, 2nd & 3rd)
'''

import time

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def nth_prime_a(n):
    """Find the nth prime number."""
    prime_count = 0
    num = 2
    while prime_count < n:
        if is_prime(num):
            prime_count += 1
        num += 1
    return num - 1

def sieve_of_eratosthenes(n):
    """Generate all primes up to n using the Sieve of Eratosthenes."""
    primes = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes

def nth_prime_b(n):
    """Find the nth prime number."""
    if n <= 0:
        return None
    primes = sieve_of_eratosthenes(10**6)  # Adjust this limit as needed
    return primes[n-1] if n <= len(primes) else None

def main():
    # Test 10, 100, 1000, 5000
    n = 5000
    start = time.time()
    print(nth_prime_a(n))
    end = time.time()
    print(end - start)
    start = time.time()
    print(nth_prime_b(n))
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()
