#!/usr/bin/python3
# Import the cmd module
import cmd

from models import storage


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

    @staticmethod
    def do_create(line):
        """Creates an instance."""
        if line == "" or line is None:  # Check if class name is missing
            print("** class name missing **")
        elif line not in storage.classes():  # Check if class doesn't exist
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()  # Create an instance
            b.save()
            print(b.id)

    @staticmethod
    def do_show(line):
        """Prints the string representation of an instance."""
        if line == "" or line is None:  # Check if class name is missing
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():  # Check if class doesn't exist
                print("** class doesn't exist **")
            elif len(words) < 2:  # Check if instance id is missing
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():  # Check if instance not found
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    @staticmethod
    def do_destroy(line):
        """Deletes an instance based on the class name and id."""
        if line == "" or line is None:  # Check if class name is missing
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():  # Check if class doesn't exist
                print("** class doesn't exist **")
            elif len(words) < 2:  # Check if instance id is missing
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():  # Check if instance not found
                    print("** no instance found **")
                else:
                    del storage.all()[key]  # Delete the instance
                    storage.save()

    @staticmethod
    def do_all(line):
        """Prints all string representation of all instances."""
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():  # Check if class doesn't exist
                print("** class doesn't exist **")
        else:
            for key in storage.all():
                print(storage.all()[key])


# Check if the file is executed and not imported
if __name__ == "__main__":
    HBNBCommand().cmdloop()
