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

        if kwargs:
            for key, value in kwargs.items():
                self.__dict__[key] = value
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

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
        self.updated_at = datetime.utcnow()

    '''Public instance method'''

    def to_dict(self):
        """
        returns dictionary containing k&v
        of __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
