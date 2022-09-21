######################################################################
# Name:       Mary Kennedy
# File:       Square.py
# Class:      CIS-1400  Summer 2017
# Chapter:    Chapter 14
# Purpose:    OOP SHAPE SQUARE

# Since set up rectangle, square is identical, so square inherit from
# rectangle which inherited from shape.
from Rectangle import Rectangle

class Square(Rectangle):

    # defing init don't need any addtional fields, so just call itself.
    # if user sets the length then also set the width, or visa versa.
    def __init__(self):
        Rectangle.__init__(self)
        
    # mutators / setters will override what is in rectangle so that if
    # they set the length then set w as well.  Note it is an L (l) not a 1
    def set_side(self, s):
        Rectangle.set_length(self, s) #Square area and perimiter can
        Rectangle.set_width(self, s)  #be computed by superclass rectangle

    
