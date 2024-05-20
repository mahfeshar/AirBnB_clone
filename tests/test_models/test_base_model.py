#!/usr/bin/python3
"""Test BaseModel"""
import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for the BaseModel module."""
    def __init__(self, *args, **kwargs):
        """Initialize the TestBaseModel class."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up method that runs before each test case."""
        pass

    def tearDown(self):
        """Tear down method that runs after each test case."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test the default behavior of creating a BaseModel instance."""
        obj = self.value()
        self.assertEqual(type(obj), self.value)

    def test_kwargs(self):
        """Test creating a BaseModel instance with keyword arguments."""
        obj = self.value()
        copy = obj.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(obj is new)

    def test_kwargsint(self):
        """Test instance with invalid integer argument."""
        obj = self.value()
        copy = obj.to_dict()
        copy[1] = 2
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """Test the string representation of a BaseModel instance."""
        obj = self.value()
        string = '[{}] ({}) {}'.format(self.name, obj.id, obj.__dict__)
        self.assertEqual(str(obj), string)

    def test_save(self):
        """Test the save method of a BaseModel instance."""
        obj = self.value()
        obj.save()
        key = self.name + '.' + obj.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], obj.to_dict())

    def test_to_dict(self):
        """Test the to_dict method of a BaseModel instance."""
        obj = self.value()
        new = obj.to_dict()
        self.assertEqual(obj.to_dict(), new)

    def test_kwargs_none(self):
        """Test instance with None as a keyword argument."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test instance with an invalid keyword argument."""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test the id attribute of a BaseModel instance."""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test the created_at attribute of a BaseModel instance."""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """Test the updated_at attribute of a BaseModel instance."""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertTrue(new.created_at == new.updated_at)
