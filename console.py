#!/usr/bin/python3
# Import the cmd module
import cmd


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


# Check if the file is executed and not imported
if __name__ == "__main__":
    HBNBCommand().cmdloop()
