# Import the json and os modules
import json
import os
# Import the classes from models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State


# Define the FileStorage class
class FileStorage:
    """
    A class that serializes instances to
    a JSON file and deserializes JSON file to instances
    """

    # Private class attributes
    __file_path = "file.json"
    __objects = {}

    # Public instance methods
    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
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
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        # Check if the JSON file exists using os.path.exists
        if os.path.exists(FileStorage.__file_path):
            # Open the JSON file in read mode
            with open(FileStorage.__file_path, "r") as f:
                # Load the json_dict from the file using json.load
                json_dict = json.load(f)
                # Loop through the json_dict
                for obj in json_dict:
                    # Get the class name from the value using its __class__ key
                    class_name = obj["__class__"]
                    # Check if the class name is valid
                    if class_name in ["BaseModel",
                                      "User",
                                      "Place",
                                      "Amenity",
                                      "City",
                                      "Review",
                                      "State"]:
                        # Import the class from models using globals()
                        cls = globals()[class_name]
                        # Create an instance of the class
                        obj = cls(**obj)
                        # Set in __objects the obj with key <obj class name>.id
                        FileStorage.__objects[obj.id] = obj
