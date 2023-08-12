#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """A class that represents a user"""

    # Define the class attributes
    email = ""           # Email attribute for the User
    password = ""        # Password attribute for the User
    first_name = ""      # First name attribute for the User
    last_name = ""       # Last name attribute for the User
