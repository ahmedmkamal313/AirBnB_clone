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

    def do_all(self, arg):
        """Prints all string representation of all instances."""

        # Split the argument by spaces
        args = arg.split()
        # Get all objects from storage using all method
        objects = storage.all()

        # Create an empty list to store the string representations
        str_list = []

        # If no argument is given, loop through all objects
        if len(args) == 0:
            for obj in objects.values():
                # Append the string representation of
                # each object to the list using str method
                str_list.append(str(obj))

        # Otherwise, get the class name from the first argument
        else:
            class_name = args[0]

            # Check if the class name is valid (only BaseModel for now),
            # print ** class doesn't exist ** otherwise
            if class_name not in class_home:
                print("** class doesn't exist **")
                return

            # Loop through all objects
            for obj in objects.values():
                # Check if the object is an instance of
                # the class using isinstance function
                if isinstance(obj, eval(class_name)):
                    # Append the string representation of each
                    # object to the list using str method
                    str_list.append(str(obj))

        # Print the list of strings
        print(str_list)

    def do_update(self, arg):
        """Update command to update an instance based on its class and id"""

        # split the arg by spaces, preserving strings between double
        # quotes using shlex module
        args = shlex.split(arg)
        # if no argument is given, print missing
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
        # get id from the second arg
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
        obj = objects[key]
        # if only two args are given, print ** attribute name missing **
        if len(args) == 2:
            print("** attribute name missing **")
            return
        # get the attr name from the third arg
        attr_name = args[2]
        # if only 3 args are given print value missing
        if len(args) == 3:
            print("** value missing **")
            return
        # get the atr value from the 4th arg
        attr_value = args[3]
        try:
            attr_value = int(attr_value)
        except ValueError:
            try:
                attr_value = float(attr_value)
            except ValueError:
                attr_value = str(attr_value).strip('"')
        setattr(obj, attr_name, attr_value)
        storage.save()


# Check if the file is executed and not imported
if __name__ == "__main__":
    HBNBCommand().cmdloop()
