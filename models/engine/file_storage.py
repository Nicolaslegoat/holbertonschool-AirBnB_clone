#!/usr/bin/python3
'''
A module that contains the Filestorage class.
'''
import json
from models.base_model import BaseModel


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

        with open(self.__file_path, "w") as file:
            json.dump(dict_json, obj)

    def reload(self):
        with open(self.__file_path, "r") as file:
            data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split(".")
