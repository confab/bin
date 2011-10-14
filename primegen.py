#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def primes(n):
    '''Return all the primes up to n.'''
    primes = [2]
    for i in range(3, n+1):
        divisible = False
        for j in primes:
            if i % j == 0:
                divisible = True
                break
        if not divisible:
            primes.append(i)
            yield i
