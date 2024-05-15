#!/usr/bin/python3
""" """
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        """ """
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        obj = self.value()
        self.assertEqual(type(obj), self.value)

    def test_kwargs(self):
        """ """
        obj = self.value()
        copy = obj.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(obj is new)

    def test_kwargsint(self):
        """ """
        obj = self.value()
        copy = obj.to_dict()
        copy[1] = 2
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """ """
        obj = self.value()
        self.assertEqual(str(obj), f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}")
