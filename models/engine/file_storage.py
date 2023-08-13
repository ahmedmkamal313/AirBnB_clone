#!/usr/bin/python3
__authors__ = "Majda Bouzayd, Ahmed Kamal"

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class FileStorage:
    """The file storage engine class, that is;
    A class that serialize and deserialize instances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return type(self).__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        if obj.id in type(self).__objects:
            raise Exception("Model already exists")
        key = obj.__class__.__name__ + "." + str(obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, obj in type(self).__objects.items():
            new_dict[key] = obj.to_dict()
        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        if not os.path.exists(type(self).__file_path):
            return
        try:
            with open(type(self).__file_path, "r") as file:
                new_dict = json.load(file)
                for key, val in new_dict.items():
                    obj = class_dict[val["__class__"]](**val)
                    type(self).__objects[key] = obj
        except Exception:
            pass
