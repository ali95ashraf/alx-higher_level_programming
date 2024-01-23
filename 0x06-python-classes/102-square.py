#!/usr/bin/python3

class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance."""
        self.size = size

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on the area of the squares."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison based on the area of the squares."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison based on the area of the squares."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison based on the area of the squares."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison based on the area of the squares."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison based on the area of the squares."""
        return self.area() >= other.area()

# Test the Square
if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
