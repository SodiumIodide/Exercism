#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Run Length Encoding Problem

Dependencies
itertools for groupby to help with encoding
re for regex capturing groups in decoding
'''

from itertools import groupby
import re
import argparse

def encode(inp):
    '''Encode a string'''
    build = []
    for character, number in groupby(inp):
        residues = list(number)
        if len(residues) > 1:
            build.append("{0}{1}".format(len(residues), character))
        else:
            build.extend(residues)
    return ''.join(build)

def decode(inp):
    '''Decode a string'''
    pattern = r'(\d*)(\D)'
    subs = re.findall(pattern, inp)
    build = ''
    for number, character in subs:
        number = number or '1'
        build += character * int(number)
    return build

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='coding', action='store_const',
                        const=decode, default=encode,
                        help='tag this to decode instead of encode')
    parser.add_argument('string', type=str, help='string to parse')
    args = parser.parse_args()
    print(args.coding(args.string))

if __name__ == '__main__':
    main()
