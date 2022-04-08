#!/usr/bin/python3
"""
Review module for Airbnb.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review the place, id, and can text """
    place_id = ""
    user_id = ""
    text = ""
