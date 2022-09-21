######################################################################
# Name:       Mary Kennedy
# File:       Rectangle.py
# Class:      CIS-1400  Summer 2017
# Chapter:    Chapter 14
# Purpose:    OOP SHAPE

# Inherit from shape class - inport the shape class therefore a
# rectangle inherits the shape class.
# The three fields and the two methods.
from Shape import Shape
 
 
class Rectangle(Shape):
 
    # Define Self intitialize.  
    def __init__(self):

        #  note double underscores - # Define fields  Adding two more fields that
        # generic shape did not have.
        self.__length = 0.0
        self.__width = 0.0

        # then define field shape to init.  
        Shape.__init__(self)

   


    # these below are known as setters or mutators, which is a procedure or now a method
    # that are private fields that can only be accessed within these files.  Every
    # private field needs to have at least one setter (mutator) and one getter (accessor).
    def set_length(self, l):
        #__length = 1
        self.__length = l
 
    def set_width(self, w):
        #__width = w
        self.__width = w

    #  Method called a getter or accessor. These methods will return something.  Every
    # private field needs to have at least one setter (mutator) and one getter (accessor).
    # In python when referencing a field, must be self.fieldname
    def get_length(self):
        return self.__length
 
    def get_width(self):
        return self.__width
    
# overriding the method of the baseclass so don't get return of 0. changed here to
    # override the shape.py file for both area and perimiter.  If don't override
# then will get whatever is in the original file known as a superclass.  
    def getArea(self):
        return self.__length * self.__width
 
    def getPerimiter(self):
        return 2.0 * self.__length + 2.0 * self.__width
 
