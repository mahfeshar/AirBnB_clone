#!/usr/bin/python3
"""Defines the BaseModel class."""

import models
import uuid
from datetime import datetime


class BaseModel:
    """that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Inistance for the Base class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            ft = '%Y-%m-%dT%H:%M:%S.%f'
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], ft)
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], ft)
            del kwargs['__class__']
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__.copy()}"

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        dic = {}
        dic = self.__dict__.copy()
        dic["__class__"] = str(type(self).__name__)
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
