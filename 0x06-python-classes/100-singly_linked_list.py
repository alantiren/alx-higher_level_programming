#!/usr/bin/python3

"""
Module :100-singly_linked_list
Define classes for a singly-linked list.
"""


class Node:
    """
    Represent a node in a singly-linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get or set the data of the Node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the Node.

        Args:
            value (int): The value to set as data.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get or set the next_node of the Node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next_node of the Node.

        Args:
            value (Node): The Node object to set as next_node.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represent a singly-linked list.
    """

    def __init__(self):
        """
        Initialize a new SinglyLinkedList.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the SinglyLinkedList in the correct sorted position.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the SinglyLinkedList.

        Returns:
            str: The string representation of the SinglyLinkedList.
        """
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
