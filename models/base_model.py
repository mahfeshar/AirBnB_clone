#!/usr/bin/python3
"""Defines the BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Inistance for the Base class"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__.copy()}"

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        # print(self.updated_at)
        # models.storage.new(self)
        models.storage.save()
        # print(models.storage.all())

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        dic = self.__dict__.copy()
        dic["__class__"] = str(type(self).__name__)
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
