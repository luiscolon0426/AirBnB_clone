#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBnB console
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ exit the programm """
        return True

    def do_EOF(self, arg):
        """ exit the programm """
        return True

    def emptyLine(self):
        """ empty line """
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
