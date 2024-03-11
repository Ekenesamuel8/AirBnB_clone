#!/usr/bin/python3
"""module for the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program."""
        print() # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
