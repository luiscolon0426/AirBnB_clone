#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    HBnB console
    """

    allowed_classes = {"BaseModel"}

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        exit the programm
        """
        return True

    def do_EOF(self, arg):
        """
        exit the programm
        """
        return True

    def emptyLine(self):
        """
        empty line
        """
        return False

    def do_create(self, arg):
        """
        creates instance
        """
        if len(arg) == 0:
            print("** class name missing **")

        elif arg != "BaseModel":
            print("** class doesn't exist **")

        elif arg:
            create_dic = {"BaseModel": BaseModel}
            new = create_dic[arg]()
            print(new.id)
            storage.new(new)
            storage.save()

    def do_show(self, arg):
        new = arg.partition(" ")
        cl_name = new[0]
        cl_id = new[2]

        if not cl_name:
            print("** class name missing **")
            return

        if cl_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return

        if not cl_id:
            print("** instance id missing **")
            return

        key = cl_name + "." + cl_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

        # elif arg:
        #     show_dic = {"BaseModel": BaseModel}
        #     instance = show_dic[arg]()

        #     line = self.parseline(arg)[0]
        #     if not isinstance(line[1], BaseModel()):
        #         print("** no instance found **")

    def do_destroy(self, arg)
    new = arg.partition(" ")
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
