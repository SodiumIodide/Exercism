#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''Leap Years'''
import argparse

def is_leap_year(yearnum):
    '''Leap year testing'''
    leapyear = False
    if yearnum % 4 == 0:
        leapyear = True
        if yearnum % 100 == 0:
            leapyear = False
            if yearnum % 400 == 0:
                leapyear = True
    return leapyear

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('year', help='year', action='store', type=int)
    args = parser.parse_args()
    leapyear = is_leap_year(args.year)
    if leapyear:
        print("{} is a leap year".format(args.year))
    else:
        print("{} is not a leap year".format(args.year))

if __name__ == '__main__':
    try:
        main()
    finally:
        print("\nProgram terminated\n")
