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
        from models import base_model
        from models import user
        from models import amenity
        from models import city
        from models import place
        from models import review
        from models import state

        list_module = {
            "BaseModel": base_model,
            "User": user,
            "Amenity": amenity,
            "City": city,
            "Place": place,
            "Review": review,
            "State": state,
        }

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:

                data = json.load(file)

                for key, value in data.items():
                    class_name = value["__class__"]

                    if class_name in list_module:
                        model_module = list_module[class_name]
                        model_class = getattr(model_module, class_name)

                    obj_instance = model_class(**value)
                    self.__objects[key] = obj_instance
