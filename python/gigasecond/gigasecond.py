#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Gigasecond Problem

Dependencies:
datetime for unit testing requirements
'''

import datetime as dt
import argparse

def add_gigasecond(initdate):
    '''Add a gigasecond to a given datetime'''
    gigasecond = 1e9  # seconds
    secinmin = 60
    secinhr = secinmin * 60
    secinday = secinhr * 24
    days = gigasecond // secinday
    gigasecond %= secinday
    hours = gigasecond // secinhr
    gigasecond %= secinhr
    minutes = gigasecond // secinmin
    gigasecond %= secinmin
    return initdate + dt.timedelta(days=days, hours=hours, minutes=minutes,
                                   seconds=gigasecond)

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('year', action='store', type=int)
    parser.add_argument('month', action='store', type=int)
    parser.add_argument('day', action='store', type=int)
    args = parser.parse_args()
    givendate = dt.datetime(args.year, args.month, args.day)
    plusgigasecond = add_gigasecond(givendate)
    print(str(plusgigasecond))

if __name__ == '__main__':
    try:
        main()
    finally:
        print("\nProgram terminated\n")
