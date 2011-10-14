#!/usr/bin/python3
# -*- coding: utf-8 -*-

def decToBin(n, char=False):
        bin = ''
        while n > 0:
            bin += str(n % 2)
            n //= 2
        if char:
            bin = bin + '0'*(8-len(bin))
        return bin[::-1]
    
def binary(n):
    try: n = int(n)
    except ValueError: pass
    if type(n) == int:
        return decToBin(n)
    else:
        result = ''
        for i in n:
                result += decToBin(ord(i), True)
        return result

def fromBinary(bin):
    bin = str(bin)
    dec = 0
    power = len(bin)-1
    for i in bin:
        dec += (int(i)*(2**power))
        power -= 1
    return dec
