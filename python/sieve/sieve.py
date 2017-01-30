#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Sieve of Eratosthenes Problem

Dependencies:
numpy for array operations
'''

import numpy as np
from sys import argv

def sieve(maxnum):
    '''Implementation of the Sieve of Eratosthenes'''
    if maxnum <= 1:
        return []
    checklist = np.ones(maxnum + 1, dtype=bool)
    for num in range(2, int(np.ceil(maxnum**0.5)) + 1):
        if checklist[num]:
            checklist[num**2::num] = 0
    return list(np.nonzero(checklist)[0][2:])

def main():
    '''Main wrapper'''
    print(sieve(int(argv[1])))

if __name__ == '__main__':
    try:
        main()
    except (IndexError, ValueError):
        print("Error in input")
        print("Usage: sieve number")
