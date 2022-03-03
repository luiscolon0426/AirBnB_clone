#!/usr/bin/python3
""" Module Users """

from models.base_model import BaseModel


class User(BaseModel):
    """ User class 
        Args:
            email (str): empty string
            password (str): empty string
            first_name (str): empty string
            last_name (str): empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
