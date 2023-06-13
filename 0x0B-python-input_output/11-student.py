#!/usr/bin/python3
# 11-student.py

"""Defines a class Student that represents a student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve.
                          If None, retrieve all attributes.

        Returns:
            dict: A dictionary representation of the student.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }


    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance based on a dictionary.

        Args:
            json (dict): A dictionary representing the student attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
