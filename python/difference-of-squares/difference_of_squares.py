#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Difference of Squares Problem

Dependencies:
functools for reduce (newly acquired Scala habits die hard)
'''
from functools import reduce
import argparse

def square_of_sum(num):
    '''Square of the sum of the numbers'''
    return reduce(lambda x, y: x + y, range(num+1))**2

def sum_of_squares(num):
    '''Sum of the squares of the numbers'''
    return reduce(lambda x, y: x + y**2, range(num+1))

def difference(num):
    '''Difference between the sum of squares and the square of the sum'''
    # The square of the sum will be larger, no need for abs
    return square_of_sum(num) - sum_of_squares(num)

def main():
    '''Main wrapper'''
    # Default to difference
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='nodiff', action='store_true',
                        help='calculate one or the other, not the difference')
    # Secondary default to square of sum: it's bigger!
    parser.add_argument('-s', dest='sumsquare', action='store_true',
                        help='calculate sum of squares, not square of sums')
    parser.set_defaults(nodiff=False, sumsquare=False)
    parser.add_argument('number', help='the number to calculate upon', type=int)
    args = parser.parse_args()
    if args.nodiff:
        if args.sumsquare:
            print("Sum of squares({}): {}".format(args.number,
                                                  sum_of_squares(args.number)))
        else:
            print("Square of sum({}): {}".format(args.number,
                                                 square_of_sum(args.number)))
    else:
        print("Difference({}): {}".format(args.number, difference(args.number)))

if __name__ == '__main__':
    main()
