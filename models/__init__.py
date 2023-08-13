#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage
__authors__ = "Majda Bouzayd, Ahmed Kamal"


storage = FileStorage()
storage.reload()
