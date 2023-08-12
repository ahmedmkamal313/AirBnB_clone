#!/usr/bin/python3
"""Defines the FileStorage class."""
import json


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
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return


...


class FileStorage:
    ...

    def _serialize_user(self, obj):
        """
        Serialize the User object.
        """
        serialized_user = {
            '__class__': obj.__class__.__name__,
            'id': obj.id,  # ID of the user
            'created_at': obj.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),  # Creation timestamp of the user
            'updated_at': obj.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),  # Update timestamp of the user
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
                                            "%Y-%m-%dT%H:%M:%S.%f")  # Convert String to datetime
        user.updated_at = datetime.strptime(serialized_user['updated_at'],
                                            "%Y-%m-%dT%H:%M:%S.%f")  # Convert String to datetime
        return user

    def _serialize(self):
        """
        Serialize all objects in __objects attribute.
        """
        ...

        for obj in objects:
            if isinstance(obj, User):
                serialized_obj = self._serialize_user(obj)
                ...

            ...

    def _deserialize(self):
        """
        Deserialize serialized objects from JSON file.
        """
        ...

        for class_name, obj_data in serialized_objs.items():
            if class_name == 'User':
                obj = self._deserialize_user(obj_data)
                ...

            ...