#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""

# Import the datetime and uuid modules
import datetime
import uuid
# Import the variable storage from models
import models


# Define The base model class
class BaseModel:
    """Base class for all models"""

    # Initialize the instance attributes
    def __init__(self, *args, **kwargs):
        """Initialize the instance attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        # If kwargs is not empty
        if kwargs:
            # loop through the kwargs dictionary
            for key, value in kwargs.items():
                # If key is __class__, skip it
                if key == "__class__":
                    continue
                # if key is created_at or updated_at convert value to datetime
                elif key == "created_at" or key == "updated_at":
                    formats = "%Y-%m-%dT%H:%M:%S.%f"
                    value = datetime.datetime.strptime(value, formats)
                # Set the instance attribute with the key and value
                setattr(self, key, value)
        # otherwise
        else:
            # Assign a unique id as a string
            self.id = str(uuid.uuid4)
            # Assign the current datetime as created_at and updated_at
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    # Define the __str__ method to print the instance information
    def __str__(self):
        """Return a formatted string with the instance information"""
        # Return a formatted string with the class name, id, and __dict__
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        # Assign the current datetime to updated at
        self.updated_at = datetime.datetime.now()
        # Call save(self) method of storage to serialize __objects to JSON file
        models.storage.save()

    # Define the to_dict method to return dictionary representation of instance
    def to_dict(self):
        """Return the dictionary representation of the instance"""
        # Create a copy of the instance __dict__
        dict_copy = self.__dict__.copy()
        # Add key __class__ with the class name of the object
        dict_copy["__class__"] = self.__class__.__name__
        # convert the created_at & updated_at to a string iso format
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        # Return the dictionary copy
        return dict_copy
