######################################################################
# Name:       Mary Kennedy
# File:       Square.py
# Class:      CIS-1400  Summer 2017
# Chapter:    Chapter 14
# Purpose:    OOP SHAPE CIRCLE

# need math fucntions so import math
# circle will inherit from shape

import math
from Shape import Shape
 
 
class Circle(Shape):

    # define init and add radius to shape fields 
    def __init__(self):
        self.__radius = 0.0
        Shape.__init__(self) #call the superclass constructor

    # private fields needs setter Don't want negative for radius
    # then if they enter a negative number then push to 0, or use
    # what they entered.
    # Called guarding code to guard against negative
    def set_radius(self, r):
        if r < 0:
            self.__radius = 0
        else:
            self.__radius = r

    # private fields needs getter
    def get_radius(self):
        return self.__radius


    # defining two new fields circumference and area so don't get 0 from Shape.py
    def getArea(self):  #rsquared * pi
        # use built in math function called pi use math.pi ** = squared.
        return math.pi * self.__radius ** 2
 
    def getPerimiter(self):  # 2pir is circumference
        # use built in math function called pi use math.pi 
        return math.pi * self.__radius * 2.0
