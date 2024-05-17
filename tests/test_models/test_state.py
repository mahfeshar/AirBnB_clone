#!/usr/bin/python3
"""Test State Module"""

from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
    """TestState class to test the State module"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'State'
        self.value = State

    def test_name(self):
        """Test the name attribute of State"""
        obj = self.value()
        self.assertEqual(type(obj.name), str)
