#!/usr/bin/python3

class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node instance."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for the data attribute."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for the next_node attribute."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the list (increasing order)."""
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)


# Test the SinglyLinkedList
if __name__ == "__main__":
    SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
