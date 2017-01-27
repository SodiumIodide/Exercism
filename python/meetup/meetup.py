#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Meetup Problem

Dependencies:
datetime for returning a date object
re for regex matching on description
'''
from datetime import date, timedelta
import re
import argparse

class MeetupDayException(Exception):
    '''Exception for a day that is out of bounds'''
    pass

def meetup_day(ynum, mnum, day, desc):
    '''Return the requested day'''
    days = {
        'mon': 0,
        'tue': 1,
        'wed': 2,
        'thu': 3,
        'fri': 4,
        'sat': 5,
        'sun': 6,
    }
    if desc == 'teenth':
        for i in range(13, 20):
            if date(ynum, mnum, i).weekday() == days[day[:3].lower()]:
                return date(ynum, mnum, i)
    requestedmonth = date(ynum, mnum, 1)
    lastday = (requestedmonth.replace(month=mnum % 12 + 1, day=1)
               - timedelta(days=1)).day
    if desc == 'last':
        for i in range(lastday, 0, -1):
            if date(ynum, mnum, i).weekday() == days[day[:3].lower()]:
                return date(ynum, mnum, i)
    pat = r'(\d+).*'
    num = int(re.search(pat, desc).group(1))
    if num > 5:
        raise MeetupDayException("Only four weeks in a month")
    cnt = 0
    for i in range(1, lastday+1):
        if date(ynum, mnum, i).weekday() == days[day[:3].lower()]:
            cnt += 1
            if cnt == num:
                return date(ynum, mnum, i)
    # If everything has failed
    raise MeetupDayException("Can't locate day")

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int, help='digit')
    parser.add_argument('month', type=int, help='digit')
    parser.add_argument('day', type=str, help='first three letters required')
    parser.add_argument('description', type=str, help='teenth, last, 1st-5th')
    args = parser.parse_args()
    print(meetup_day(args.year, args.month, args.day, args.description))

if __name__ == '__main__':
    main()
