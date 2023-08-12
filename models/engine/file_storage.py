#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        # Create a key with the format <obj class name>.id
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # Set the value as the obj
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        # Create an empty dictionary to store
        # the JSON representation of each object
        json_dict = {}
        # Loop through the __objects dictionary
        for key, value in FileStorage.__objects.items():
            # Convert each object to a dictionary using its to_dict method
            json_dict[key] = value.to_dict()
        # Open the JSON file in write mode
        with open(FileStorage.__file_path, "w") as f:
            # Dump the json_dict to the file using json.dump
            json.dump(json_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        # Check if the JSON file exists using os.path.exists
        if os.path.exists(FileStorage.__file_path):
            # Open the JSON file in read mode
            with open(FileStorage.__file_path, "r") as f:
                # Load the json_dict from the file using json.load
                json_dict = json.load(f)
                # Loop through the json_dict
                for key, value in json_dict.items():
                    # Get the class name from the value using its __class__ key
                    class_name = value["__class__"]
                    # Import the class from models using globals()
                    cls = globals()[class_name]
                    # Create an instance of class using its **value as kwargs
                    obj = cls(**value)
                    # Set in __objects the obj with key <obj class name>.id
                    FileStorage.__objects[key] = obj

    def _serialize_user(self, obj):
        """
        Serialize the User object.
        """
        serialized_user = {
            '__class__': obj.__class__.__name__,
            'id': obj.id,  # ID of the user
            'created_at': obj.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            'updated_at': obj.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            'email': obj.email,  # Email of the user
            'password': obj.password,  # Password of the user
            'first_name': obj.first_name,  # First name of the user
            'last_name': obj.last_name  # Last name of the user
        }
        return serialized_user

    def _deserialize_user(self, serialized_user):
        """
        Deserialize the User object.
        """
        user = User()
        user.__dict__.update(serialized_user)
        user.created_at = datetime.strptime(serialized_user['created_at'],
                                            "%Y-%m-%dT%H:%M:%S.%f")
        user.updated_at = datetime.strptime(serialized_user['updated_at'],
                                            "%Y-%m-%dT%H:%M:%S.%f")
        return user

    def _serialize(self):
        """
        Serialize all objects in __objects attribute.
        """

        for obj in objects:
            if isinstance(obj, User):
                serialized_obj = self._serialize_user(obj)

    def _deserialize(self):
        """
        Deserialize serialized objects from JSON file.
        """
        for class_name, obj_data in serialized_objs.items():
            if class_name == 'User':
                obj = self._deserialize_user(obj_data)
