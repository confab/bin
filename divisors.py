#! /usr/bin/python

def divisors(n):
    '''Find the divisors of n.'''
    
    divs = {1, n}
    
    low = 2
    high = n
    
    while low < high:
        if (high/low)%1 == 0:
            high = int(high/low)
            divs.update([low, high])
        low += 1
    divs = list(divs)
    divs.sort()
    return divs

def main():
    from sys import argv
    print(divisors(int(argv[1])))

if __name__ == '__main__':
    main()
