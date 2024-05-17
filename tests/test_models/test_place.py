#!/usr/bin/python3
"""Test Place Module"""

from models.place import Place
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):
    """Test Place class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'Place'
        self.value = Place

    def test_city_id(self):
        """Test city_id attribute"""
        obj = self.value()
        self.assertEqual(type(obj.city_id), str)

    def test_user_id(self):
        """Test user_id attribute"""
        obj = self.value()
        self.assertEqual(type(obj.user_id), str)

    def test_name(self):
        """Test name attribute"""
        obj = self.value()
        self.assertEqual(type(obj.name), str)

    def test_description(self):
        """Test description attribute"""
        obj = self.value()
        self.assertEqual(type(obj.description), str)

    def test_number_rooms(self):
        """Test number_rooms attribute"""
        obj = self.value()
        self.assertEqual(type(obj.number_rooms), int)

    def test_number_bathrooms(self):
        """Test number_bathrooms attribute"""
        obj = self.value()
        self.assertEqual(type(obj.number_bathrooms), int)

    def test_max_guest(self):
        """Test max_guest attribute"""
        obj = self.value()
        self.assertEqual(type(obj.max_guest), int)

    def test_price_by_night(self):
        """Test price_by_night attribute"""
        obj = self.value()
        self.assertEqual(type(obj.price_by_night), int)

    def test_latitude(self):
        """Test latitude attribute"""
        obj = self.value()
        self.assertEqual(type(obj.latitude), float)

    def test_longitude(self):
        """Test longitude attribute"""
        obj = self.value()
        self.assertEqual(type(obj.longitude), float)

    def test_amenity_ids(self):
        """Test amenity_ids attribute"""
        obj = self.value()
        self.assertEqual(type(obj.amenity_ids), list)
