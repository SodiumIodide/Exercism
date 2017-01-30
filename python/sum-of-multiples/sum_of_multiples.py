#!usr/bin/env python3
# -*- coding: utf-8 -*-

'''Sum of Multiples Problem'''

def sum_of_multiples(maxnum, inptargets):
    '''
    Provide the sum of the multiples of a given set of numbers,
    up to but not including the given maximum number.
    '''
    multiples = []
    targets = [i for i in inptargets if i != 0]
    for number in range(maxnum):
        for target in targets:
            if number % target == 0:
                multiples.append(number)
    return sum(set(multiples))
