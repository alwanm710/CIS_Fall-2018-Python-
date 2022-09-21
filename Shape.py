######################################################################
# Name:       Mary Kennedy 
# File:       Shape.py
# Class:      CIS-1400  Summer 2017
# Chapter:    Chapter 14
# Purpose:    OOP SHAPE CLASS 

# Class or concept of a shape, file and class name should match
# now when you see self think OOP.  Concepts not a particular shape.  When
# create new shape then need new instance.  Of the class circle concept but
# need seperate attrtibutes in the program

class Shape:

# define fields (former variables)  # whatever shape it is all shapes have
# color,area, and perimiter
    def __init__(self):
        self.__color = 'None'
        self.__area = 0.0
        self.__perimiter = 0.0
        

# define function area (A = LxW) but since don't know this yet, return a 0
# inititally
    def getArea(self):
        return 0.0

# define function perimiter = C = 2L*2W, but since don't know this yet,
# return a 0
    def getPerimeter(self):
        return 0.0

