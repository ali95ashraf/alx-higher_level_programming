#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A Square class."""

    def __init__(self, size):
        """Initialize a Square instance."""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
