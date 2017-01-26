#!user/bin/env python3
# -*- coding: utf-8 -*-
'''Clock Problem'''

import argparse

class Clock:
    '''Clock object'''
    def __init__(self, hour=0, minute=0):
        while hour < 0:
            hour += 24
        while minute < 0:
            minute += 60
            hour -= 1
        while minute > 59:
            minute -= 60
            hour += 1
        hour %= 24
        self.hour = hour
        self.minute = minute

    def add(self, minute):
        '''Add or subtract minutes from clock'''
        self.minute += minute
        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
        while self.minute > 59:
            self.minute -= 60
            self.hour += 1
        self.hour %= 24
        return self

    def __str__(self):
        return "{0:02}:{1:02}".format(self.hour, self.minute)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('hour', help='hour', action='store', type=int)
    parser.add_argument('minute', help='minute', action='store', type=int)
    parser.add_argument('-a', '--add', help='add minutes', action='store', type=int)
    args = parser.parse_args()
    if args.add:
        print(str(Clock(args.hour, args.minute).add(args.add)))
    else:
        print(str(Clock(args.hour, args.minute)))

if __name__ == '__main__':
    try:
        main()
    finally:
        print("\nProgram terminated\n")
