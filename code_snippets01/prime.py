#!/usr/bin/python3

# Finding prime numbers using the else clause
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
        else:
            print(n, "is a prime number.")