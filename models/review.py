#!/usr/bin/python3
# models/review.py
from models.base_model import BaseModel


class Review(BaseModel):
    """A class that represents a review"""

    place_id = ""
    user_id = ""
    text = ""
