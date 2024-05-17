#!/usr/bin/python3
"""Test Review Module"""

from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    """Test Review class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'Review'
        self.value = Review

    def test_place_id(self):
        """Test place_id attribute"""
        obj = self.value()
        self.assertEqual(type(obj.place_id), str)

    def test_user_id(self):
        """Test user_id attribute"""
        obj = self.value()
        self.assertEqual(type(obj.user_id), str)

    def test_text(self):
        """Test text attribute"""
        obj = self.value()
        self.assertEqual(type(obj.text), str)
