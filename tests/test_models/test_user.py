#!/usr/bin/python3
"""Test User Module"""

from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """Test case for the User class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'User'
        self.value = User

    def test_email(self):
        """Test the email attribute of User"""
        obj = self.value()
        self.assertEqual(type(obj.email), str)

    def test_password(self):
        """Test the password attribute of User"""
        obj = self.value()
        self.assertEqual(type(obj.password), str)

    def test_first_name(self):
        """Test the first_name attribute of User"""
        obj = self.value()
        self.assertEqual(type(obj.first_name), str)

    def test_last_name(self):
        """Test the last_name attribute of User"""
        obj = self.value()
        self.assertEqual(type(obj.last_name), str)
