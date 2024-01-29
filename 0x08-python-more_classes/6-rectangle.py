#!/usr/bin/python3
"""
Defines a class Rectangle
"""

class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message for every deletion of a Rectangle.""" 
        print("Bye rectangle...")

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self._width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self._height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """returns the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)

    def str_(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self._width != 0 and self._height != 0:
            string += "\n".join(["#" * self._width for j in range(self._height)])
        return string

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({}, {})".format(self._width, self._height)
