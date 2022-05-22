"""
CSE102-Advanced Programming
Tutorial 9
Yubo Cai
date: 12/05/2022
"""
import random


# Exercise 1
def is_prime(n, k=32):
    # we try to distinct the prime numbers
    # we first set number of r and d
    r = 0
    d = n - 1

    if n <= 3:
        return True

    while d % 2 == 0:
        d = d // 2
        r += 1

    # we use the Miller-Rabin test and excute for k times
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # let x =a^d mod n

        is_composite = True
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                is_composite = False
                break

        if is_composite is True:
            return False

    return True


# Exercise 2
def genprime(l):
    """
    It’s now time to generate our big primes. For that, we are going to write a function genprime(l) that generates a prime number of (roughly) l bits. 
    The function starts by generating a number n of l bits where each bit was randomly chosen – think about the bit-masking operations you have previsouly seen! 
    We however force the LSB and MSB bits to be 1 (s.t. the number is odd, and is really l bits long). 
    Then, the function returns the first number n+2i that is prime where i ranges over {0,1,2,3,…}.
    """
    n = 1
    for i in range(l - 2):
        n = n << 1
        n += random.randint(0, 1)

    n = n << 1
    n += 1
    m = 0
    while True:
        if is_prime(n + 2 * m):
            return n + 2 * m
        m += 1

# Exercise 3
def egcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0

def genmod(p,q):
    cod = (p-1)*(q-1)
    while True:
        e = random.randint(2, cod-1)    
        gcd, u, v = egcd(e, cod)
        if gcd != 1:
            continue
        
        elif u < 0:
            while u < 2 or u > cod:
                u += cod
        pub = p*q
        return ((pub,e), u)
    
def keygen(l):
    return genmod(genprime(l//2),genprime(l//2))

def enc(m, pkey):
    # encode the message
    p_key1 = pkey[1]
    p_key2 = pkey[0]
    return pow(m, p_key1, p_key2)

def dec(c, pkey, skey):
    # decode the message
    return pow(c,skey,pkey[0])