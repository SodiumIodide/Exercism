#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''Hamming Distance Problem'''

import argparse

def distance(seq1, seq2):
    '''
    Hamming distance calculation
    Raises ValueError on mismatched lengths
    '''
    if len(seq1) != len(seq2):
        raise ValueError
    return sum(1 for a, b in zip(seq1, seq2) if a != b)

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('seq1', help='First sequence', action='store')
    parser.add_argument('seq2', help='Second sequence', action='store')
    args = parser.parse_args()
    try:
        dist = distance(args.seq1, args.seq2)
        print("Hamming distance: {}".format(dist))
    except ValueError:
        print("Input must be of the same length")

if __name__ == '__main__':
    main()
