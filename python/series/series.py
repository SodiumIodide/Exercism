#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''Series Problem'''

import argparse

def slices(inpstr, size):
    '''Return a "rolling" or "sliding" operator on input string'''
    if size == 0 or size > len(inpstr):
        raise ValueError("Invalid size input")
    if not inpstr.isdigit():
        raise ValueError("Invalid string input")
    return [list(map(lambda x: int(x), inpstr[i:i+size]))
            for i in range(len(inpstr) - (size - 1))]

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('string', help='string of numbers to operate on')
    parser.add_argument('length', type=int, help='size of window')
    args = parser.parse_args()
    try:
        parts = slices(args.string, args.length)
        for part in parts:
            print(''.join(str(x) for x in part))
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()
