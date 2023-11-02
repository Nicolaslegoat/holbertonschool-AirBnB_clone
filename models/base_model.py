#!/usr/bin/python3
"""
Project AirBnB Clone
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    defines all common attributes
    """
    def __init__(self):
        """
        Initializer for BaseModel class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representaton of a BaseModel
        """
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instances attribute
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
