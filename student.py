# -*- coding: utf-8 -*-
import unittest
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):

        if  80 <= self.score <=100:
            return 'A'

        elif 60<= self.score <80:
            return 'B'

        elif  0 <=self.score <60:
            return "C"

        else :
            print("the format of note is disqualification ")
            raise ValueError("Vvvvv")


sss = Student("sss",-1)
print(sss.get_grade())
