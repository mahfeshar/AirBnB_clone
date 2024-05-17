#!/usr/bin/python3
"""The module for Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The review that inherit from BaseModel"""
    # it will be the Place.id
    place_id = ''
    # it will be the User.id
    user_id = ''
    text = ''
