#!/usr/bin/python3
"""This module for a User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This defines a user"""
    email = ''
    password = ''
    first_time = ''
    last_name = ''
