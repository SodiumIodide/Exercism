#!usr/bin/env python3
# -*- coding: utf-8 -*-

'''Largest Series Product Problem'''

import argparse

# Reusing code from a previous problem: series
def slices(inpstr, size):
    '''Return a "rolling" or "sliding" operator on input string'''
    if size <= 0 or size > len(inpstr):
        raise ValueError("Invalid size input")
    if not inpstr.isdigit():
        raise ValueError("Invalid string input")
    return [list(map(lambda x: int(x), inpstr[i:i+size]))
            for i in range(len(inpstr) - (size - 1))]

def largest_product(inpstr, size):
    '''Return the largest product of a rolling operator over a digital series'''
    if size == 0:
        return 1
    try:
        series = slices(inpstr, size)
    except ValueError as vale:
        raise vale
    products = []
    for chain in series:
        # Initial value of unity
        product = 1
        for digit in chain:
            product *= digit
        products.append(product)
    return max(products)

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('string', help='string of numbers to operate on')
    parser.add_argument('length', type=int, help='size of window')
    args = parser.parse_args()
    try:
        print(largest_product(args.string, args.length))
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()
