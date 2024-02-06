#!/usr/bin/python3
"""Module for Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A Rectangle class."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance."""
        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(r.area())
