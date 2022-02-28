#!/usr/bin/python3
""" Base Model module for airbnb clone """

import uuid
from datetime import datetime
import json
from xmlrpc.client import _iso8601_format


class BaseModel:
    """
    Defining BaseModel class that define all
    common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the baseModel class
        str: name of the user
        number: id number
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = _iso8601_format(datetime.now())
            self.updated_at = _iso8601_format(datetime.now())
        else:
            for key, value in kwargs.items():
                self.__dict__[key] = value
            del self.__dict__['__class__']
            self.__dict__["created_at"] = datetime.strptime(
                self.__dict__["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """
        Print class name, id & dictionary
        """
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    '''Public instance method'''

    def save(self):
        """
        Updates the instance to the current
        day and time
        """
        self.updated_at = datetime.now()

    '''Public instance method'''

    def to_dict(self):
        """
        returns dictionary containing k&v
        of __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
