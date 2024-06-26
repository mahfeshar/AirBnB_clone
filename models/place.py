#!/usr/bin/python3
"""The module for place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """The place that inherit from BaseModel"""
    #  it will be the City.id
    city_id = ''
    # it will be the User.id
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    # it will be the list of Amenity.id later
    amenity_ids = []
