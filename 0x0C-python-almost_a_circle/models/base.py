#!/usr/bin/python3
# base.py
"""Defines a base class."""


class Base:
    """Represent the base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base object.

        Args:
            id (int): The identity of the new Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a file in JSON format.

        Args:
            list_objs (list): A list of objects to be saved.
        """
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation.

        Args:
            json_string (str): A JSON string representation.

        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance of the class and update it with a dictionary.

        Args:
            **dictionary (dict): Dictionary containing the attributes of the object.

        Returns:
            object: The newly created object.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load a list of objects from a file in JSON format.

        Returns:
            list: A list of objects loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dict_list = cls.from_json_string(json_data)
                obj_list = []
                for dictionary in dict_list:
                    obj = cls.create(**dictionary)
                    obj_list.append(obj)
                return obj_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects to be saved.
        """
        import csv
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if list_objs is not None and len(list_objs) > 0:
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.width, obj.height, obj
