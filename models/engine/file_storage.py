#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic = {}
        dic.update(FileStorage.__objects)
        for key, value in dic.items():
            dic[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf=8") as f:
            json.dump(dic, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                temp = json.load(f)
                for key, value in temp.items():
                    self.__objects[key] = classes[value['__class__']](**value)
            # with open(self.__file_path, 'r', encoding="utf-8") as f:
            #     for o in json.load(f).values():
            #         name = o["__class__"]
            #         del o["__class__"]
            #         self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
