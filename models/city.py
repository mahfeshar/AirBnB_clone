#!/usr/bin/python3
"""The module for city"""
from models.base_model import BaseModel


class City(BaseModel):
    """The city that inherit from BaseModel"""
    # it will be the State.id
    state_id = ''
    name = ''
