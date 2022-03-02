#!/usr/bin/python3
"""
Class to serialize instances to a JSON file and
deserializes JSON file to instances
"""


from models.base_model import BaseModel
import os
import json

class FileStorage:
    """
    Class for serialization and deserialazation
        Args:
            __filepath_path (str): string-path to JSON file
            __object (dict): empty but will store all the objects by
            <class name>.id
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """
        Docstring all method that returns
        the dictionary __object
        """
        return self.__objects

    def new(self, obj):
        """
        Docstring new method that sets in __objects
        the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Docstring save method that serializes __objects
        to the JSON file
        """
        save_dic = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                save_dic[key] = value.to_dict()
            json.dump(save_dic, f)

    def reload(self):
        """
        Docstring reload method that deserializes the JSON file
        to __objects (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn't exist, no exception
        should be raised)
        """
        load_dic = {}
        isFile = os.path.isfile(self.__file_path)
        if isFile:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                load = f.read()
                new_dict = json.loads(load)
                for key, value in new_dict.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
