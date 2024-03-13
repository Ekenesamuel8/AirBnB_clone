#!/usr/bin/python3
"""module for the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_create(self, command):
        """creates an object"""
        if not command:
            print("** class name missing **")
            return
        try:
            new_instance = eval(command)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, command):
        """Prints the string representation of an instance based on the class name and id."""
        command = command.split()
        if not command:
            print("** class name missing **")
            return
        try:
            class_name = command[0]
            if len(command) < 2:
                print("** instance id missing **")
                return
            instance_id = command[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, command):
        """Deletes an instance based on the class name and id."""
        command = command.split()
        if not command:
            print("** class name missing **")
            return
    
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")


    def do_EOF(self, line):
        """EOF command to exit the program."""
        print() # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
