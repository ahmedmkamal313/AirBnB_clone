#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""

# Import the datetime and uuid modules
import datetime
import uuid

# Define The base model class
class BaseBodel:
    """Base class for all models"""

    # Initialize the instance attributes
    def __init__(self):
        # Assign a unique id as a string
        self.id = str(uuid.uuid4)
        # Assign the current datetime as created_at and updated_at
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    # Define the __str__ method to print the instance information
    def __str__(self):
        """Return a formatted string with the instance information"""
        # Return a formatted string with the class name, id, and __dict__
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


