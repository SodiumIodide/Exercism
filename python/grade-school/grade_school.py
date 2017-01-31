# -*- coding: utf-8 -*-

'''Grade School Problem'''

class School:
    '''A typical average everyday normal school'''
    def __init__(self, name='Generic School'):
        self.name = name
        # I do not know if Python has a way to limit access to mutable data,
        # other than using the quote-unquote "private" notation.
        self.__roster = {}

    def grade(self, gradenum):
        '''Return roster for a given grade'''
        return self.__roster.get(gradenum, {})

    def add(self, student, gradenum):
        '''Add a student to a grade'''
        if not self.__roster.get(gradenum):
            self.__roster[gradenum] = [student]
        else:
            self.__roster[gradenum].append(student)

    def sort(self):
        '''Alphabetical list by grade'''
        return [(grade, tuple(sorted(self.__roster[grade])))
                for grade in self.__roster]
