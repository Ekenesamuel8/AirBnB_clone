#!/usr/bin/python3
"""module for the command interpreter."""
import cmd
from models.base_model import BaseModel


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
        """Prints the string representation of an instance
           based on the class name and id."""
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
            class_name = command[0]
            if len(command) < 2:
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

    def do_all(self, command):
        """Prints all string representations of
           instances based on the class name."""
        command = command.split()
        obj_list = []
        try:
            if not command:
                for key, value in storage.all().items():
                    obj_list.append(str(value))
                print(obj_list)
                return

            class_name = command[0]
            for key, value in storage.all().items():
                if class_name in key:
                    obj_list.append(str(value))
            if obj_list:
                print(obj_list)
            else:
                print("** class doesn't exist **")

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, command):
        """Updates an instance based on the class name
           and id by adding or updating attribute."""
        command = command.split()
        if not command:
            print("** class name missing **")
            return

        try:
            class_name = command[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
                return

            if len(command) < 2:
                print("** instance id missing **")
                return

            instance_id = command[1]
            key = "{}.{}".format(class_name, instance_id)

            if key not in storage.all():
                print("** no instance found **")
                return

            if len(command) < 3:
                print("** attribute name missing **")
                return

            attribute_name = command[2]

            if len(command) < 4:
                print("** value missing **")
                return

            attribute_value = command[3]

            obj = storage.all()[key]
            if hasattr(obj, attribute_name):
                attribute_value = type(getattr(obj, attribute_name))(attribute_value)
                setattr(obj, attribute_name, attribute_value)
                storage.save()
            else:
                print("** attribute doesn't exist **")

        except Exception as e:
            print(e)

    def do_EOF(self, line):
        """EOF command to exit the program."""
        print() # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
