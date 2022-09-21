######################################################################
# Name:       Mary Kennedy
# File:       ShapeProgram.py
# Class:      CIS-1400  Summer 2017
# Chapter:    Chapter 14
# Purpose:    OOP SHAPE PROGRAM


# add from ____ import  _____ as needed 
from Rectangle import Rectangle
from Square import Square
from Circle import Circle
 
 
def main():
    # shape1 = Rectangle()  # changing program and needed for shape.
    # shape1 = Square()  # changing program and needed for shape.
    shape1 = Circle()  # changing program and needed for shape.
    shape2 = Rectangle()   # adding in additional circle instance
    shape3 = Square()   # adding in additional circle instance
    

    # - note thise below are private fields so they must match the setter or
    # mutator  which is a procedure or now a method.  See Rectangle.py for
    # setters and getters.  
    
    # shape1.set_length(5.0)  # set length doesn't exist for a circle
                              # so comment out
    # shape1.set_width(10.0)  # comment out for circle since set_width
                              # doesn't exist
    shape1.set_radius(5.0)
    shape1.color = 'Red'
    shape2.set_length(2.0)
    shape2.set_width(3.0)
    shape2.color = 'Blue'
    shape3.set_side(2.0)
    shape3.color = 'Green'
    
 
    print('shape 1')
    print('Color:        ', shape1.color)
    print('Radius:       ', shape1.get_radius())
    print('Area:         ', shape1.getArea())
    print('Perimiter:    ', shape1.getPerimiter())
    print('shape 2')
    print('Color:        ', shape2.color)
    print('Length:       ', shape2.get_length())  
    print('Width:        ', shape2.get_width())  
    print('Area:         ', shape2.getArea())
    print('Perimiter:    ', shape2.getPerimiter())
    print('shape 3')
    print('Color:        ', shape3.color)
    print('Side:         ', shape3.get_length()) 
    print('Area:         ', shape3.getArea())
    print('Perimiter     ', shape3.getPerimiter())

    
    
 
main()
