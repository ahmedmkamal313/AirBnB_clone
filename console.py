#!/usr/bin/python3
# Import the cmd module
import cmd

from models import storage

# Define the HBNBCommand class that inherits from cmd.Cmd
class User:
    pass


class HBNBCommand(cmd.Cmd):
    """A command interpreter for the AirBnB clone project"""

    # Set the custom prompt to (hobnob)
    prompt = "(hbnb) "

    # Define the quit command to exit the program
    @staticmethod
    def do_quit():
        """Quit command to exit the program"""
        # Return True to stop the cmdloop
        return True

    # Define the EOF command to exit the program
    @staticmethod
    def do_EOF():
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

    # noinspection PyShadowingNames
    class Command:
        ...

        def do_show(self, arg):
            """Show command"""
            ...
            # Check if the argument is referencing a User
            if arg[0] == "User":
                self.show(arg[1])  # Call the show method with User class and the specified argument
            ...

        @staticmethod
        def do_create(arg):
            """Create command"""
            ...
            # Check if the argument is referencing a User
            if arg[0] == "User":
                user = User()  # Create a new User instance with the provided kwargs
                user.save()  # Save the user instance
                print(user.id)  # Print the user ID
            ...

        def do_destroy(self, arg):
            """Destroy command"""
            ...
            # Check if the argument is referencing a User
            if arg[0] == "User":
                self.destroy(User, arg[1])  # Call the destroy method with User class and the specified argument
            ...

        def do_update(self, arg):
            """Update command"""
            ...
            # Check if the argument is referencing a User
            if arg[0] == "User":
                self.update(User, arg[1], arg[2], arg[3],
                            arg[4])  # Call the update method with User class and the specified arguments
            ...

        def do_all(self, arg):
            """All command"""
            ...
            # Check if the argument is referencing a User
            if arg[0] == "User":
                self.all(User)  # Call the all method with User class
            ...

        def show(self, param):
            pass

        def destroy(self, User, param):
            pass

        def update(self, User, param, param1, param2, param3):
            pass

        def all(self, User):
            pass


# Check if the file is executed and not imported
if __name__ == "__main__":
    HBNBCommand().cmdloop()
