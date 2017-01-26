#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''Bob Problem'''

import argparse

def hey(what):
    '''Freakin' Bob'''
    saywhat = what.strip()
    punct = {
        '?': 'Sure.',
    }
    if saywhat == '':
        return 'Fine. Be that way!'
    if saywhat[:-1].isupper():
        return 'Whoa, chill out!'
    response = punct.get(saywhat[-1], 'Whatever.')
    return response

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('phrase', action='store', help='talk to Bob', type=str)
    args = parser.parse_args()
    print(hey(args.phrase))

if __name__ == '__main__':
    main()
