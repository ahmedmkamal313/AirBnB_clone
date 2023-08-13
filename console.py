#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""


import cmd
import shlex
import models
import json
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_home = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


# Define the HBNBCommand class that inherits from cmd.Cmd
class HBNBCommand(cmd.Cmd):
    """A command interpreter for the AirBnB clone project"""

    # Set the custom prompt to (hbnb)
    prompt = "(hbnb) "

    # Define the quit command to exit the program

    def do_quit(self, arg):
        """Quit command to exit the program"""
        # Return True to stop the cmdloop
        return True

    # Define the EOF command to exit the program
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        # Print a new line
        print()
        # Return True to stop the cmdloop
        return True

    # Define the help command to show the available commands
    def do_help(self, arg):
        """Help command to show the available commands"""
        # Call the superclass method with the same name
        super().do_help(arg)

    # Define an emptyline method to do nothing when an empty line is entered
    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    # Define the create command to create a new instance of the a class
    # and print its id
    def do_create(self, arg):
        """Creates an instance and prints its id"""
        # Split the argument by spaces
        args = arg.split()
        # If no argument is given, print ** class name missing **
        if len(args) == 0:
            print("** class name missing **")
            return
        # get the class name of the first argument
        class_name = args[0]
        # check if the class name if valid
        if class_name not in class_home:
            print("** class doesn't exist **")
            return
        # create an instance of the class using eval
        obj = eval(class_name)()
        # save the instance to the JSON file using storage
        storage.save()
        # print the id of the instance
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        # Split the argument by spaces
        args = arg.split()
        # If no argument is given, print ** class name missing **
        if len(args) == 0:
            print("** class name missing **")
            return
            # get the class name of the first argument
        class_name = args[0]
        # check if the class name if valid
        if class_name not in class_home:
            print("** class doesn't exist **")
            return
        # if only one arg is given, print is missing
        if len(args) == 1:
            print("** instance id missing **")
            return
        # get the id from the second argument
        _id = args[1]
        # Create a key with the format <class name>.id
        key = "{}.{}".format(class_name, _id)
        # Get all objects from storage using all method
        objects = storage.all()
        # Check if the key exists in objects dictionary,
        # print ** no instance found ** otherwise
        if key not in objects:
            print("** no instance found **")
            return
        # Get the object from objects dictionary using key
        obj = objects[key]
        # Print the string representation of object using str method
        print(str(obj))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        # Split the argument by spaces
        args = arg.split()
        # If no argument is given, print ** class name missing **
        if len(args) == 0:
            print("** class name missing **")
            return
        # Get the class name from the first argument
        class_name = args[0]
        # Check if the class name is valid (only BaseModel for now)
        if class_name not in class_home:
            print("** class doesn't exist **")
            return
        # If only one argument is given, print ** instance id missing **
        if len(args) == 1:
            print("** instance id missing **")
            return
        # Get the id from the second argument
        _id = args[1]
        # Create a key with the format <class name>.id
        key = "{}.{}".format(class_name, _id)
        # Get all objects from storage using all method
        objects = storage.all()
        # Check if the key exists in objects dictionary,
        # print ** no instance found ** otherwise
        if key not in objects:
            print("** no instance found **")
            return
        # Delete the object from objects dictionary using key
        del objects[key]
        # Save the change to the JSON file using storage
        storage.save()

    def do_all(self, line):
        """Print all instances in string representation"""
        # Create an empty list to store the objects
        objects = []
        # Check if the line is empty
        # Print all the values in the storage as strings
        if line == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            # Split the line by spaces
            st = line.split(" ")
            # Check if the first element is a valid class name
            if st[0] not in class_home:
                print("** class doesn't exist **")
            else:
                # Loop through all the items in the storage
                for key, value in storage.all().items():
                    # Split the key by dots
                    clas = key.split(".")
                    # Check if the first element matches the class name
                    if clas[0] == st[0]:
                        objects.append(str(value))
                print(objects)

        def do_update(self, line):
        """Update a class instance of a given id by adding or updating"""
        arr = line.split()
        if len(arr) < 1:
            print("** class name missing **")
            return
        elif arr[0] not in class_home:
            print("** class doesn't exist **")
            return
        elif len(arr) < 2:
            print("** instance id missing **")
            return
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            elif len(arr) < 3:
                print("** attribute name missing **")
                return
            elif len(arr) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], arr[2], arr[3])
                storage.save()

        def do_count(self, line):
        """Prints the number of instances of a given class"""
        # Get the class object from the global namespace
        class_object = globals().get(line, None)
        if class_object is None:
            # Print an error message if the class does not exist
            print("** class doesn't exist **")
            return
        # Initialize the count to zero
        count = 0
        # Loop through all the objects in the storage
        for obj in storage.all().values():
            # Check if the object belongs to the given class
            if obj.__class__.__name__ == line:
                # Increment the count by one
                count += 1
        # Print the count to the standard output
        print(count)

    def default(self, line):
        """Defult fnction that represent default values"""
        if line is None:
            return
        cmdPattern = r"^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        paramsPattern = """^"([^"]+)"(?:,\\s*(?:"([^"]+)"|""" + \
                        """(\\{[^}]+\\}))(?:,\\s*(?:("?[^"]+"?)))?)?"""
        m = re.match(cmdPattern, line)
        if not m:
            super().default(line)
            return
        mName, method, params = m.groups()
        m = re.match(paramsPattern, params)
        params = [item for item in m.groups() if item] if m else []

        cmd = " ".join([mName] + params)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'show':
            return self.do_show(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
            return self.do_update(cmd)


# Check if the file is executed and not imported
if __name__ == "__main__":
    HBNBCommand().cmdloop()
