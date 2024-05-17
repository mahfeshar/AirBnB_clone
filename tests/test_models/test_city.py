#!/usr/bin/python3
"""Test City Module"""
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """TestCity class to test the City module"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'City'
        self.value = City

    def test_state_id(self):
        """Test the state_id attribute of City"""
        obj = self.value()
        self.assertEqual(type(obj.state_id), str)

    def test_name(self):
        """Test the name attribute of City"""
        obj = self.value()
        self.assertEqual(type(obj.name), str)
