#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Pangram Problem

Dependencies:
string for alphabet
'''

from string import ascii_lowercase
import argparse

def is_pangram(inp):
    '''Check if string input is pangram'''
    for letter in ascii_lowercase:
        if letter not in inp.lower():
            return False
    return True

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('string', help='input string', action='store')
    args = parser.parse_args()
    if is_pangram(args.string):
        print("\"{}\" is a pangram".format(args.string))
    else:
        print("\"{}\" is not a pangram".format(args.string))

if __name__ == '__main__':
    try:
        main()
    finally:
        print("\nProgram terminated\n")
