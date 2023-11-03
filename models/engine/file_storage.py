#!/usr/bin/python3
""" file_storage module that contains the FileStorage class
"""
from models.base_model import BaseModel
import json
import os
import models


class FileStorage:
    '''A File storage class.'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary
        """
        return (self.__objects)

    def new(self, obj):
        """
        Set in object with a key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        dict_json = {}
        for key, obj in self.__objects.items():
            dict_json[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(dict_json))

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    data = json.loads(file.read())
                except json.decoder.JSONDecodeError:
                    data = {}
            for key, value in data.items():
                self.__objects[key] = eval(value["__class__"])(**value)
