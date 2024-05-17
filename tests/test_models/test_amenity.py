#!/usr/bin/python3
"""Test Amenity Module"""

from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """Test case for the Amenity class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'Amenity'
        self.value = Amenity

    def test_name(self):
        """Test the name attribute of Amenity"""
        obj = self.value()
        self.assertEqual(type(obj.name), str)
