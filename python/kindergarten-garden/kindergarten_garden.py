# -*- coding: utf-8 -*-

'''Kindergarten Garden Problem'''

class Garden():
    '''A beautiful garden of ACTUAL plants'''
    __STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                  'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    __PLANTS = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets',
    }
    def __init__(self, garden, **kwargs):
        self.students = sorted(kwargs.get('students', self.__STUDENTS))
        self.garden = garden.splitlines()

    def plants(self, student):
        '''The plants assigned to a given student'''
        ind = self.students.index(student) * 2  # Students get two plants / row
        # Garden has two rows
        assignedplants = [self.garden[0][ind], self.garden[0][ind + 1],
                          self.garden[1][ind], self.garden[1][ind + 1]]
        fullplants = [self.__PLANTS.get(plant) for plant in assignedplants]
        return fullplants
