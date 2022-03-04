#!/usr/bin/python3
"""
City module for Airbnb
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ city class with id and name """
    state_id = ""
    name = ""
