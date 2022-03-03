#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    HBnB console
    """

    allowed_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

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

    def do_destroy(self, arg):
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
            print("** instance is missing **")
            return

        key = cl_name + "." + cl_id

        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        all_list = []

        if arg:
            split = arg.split(" ")[0]
            if arg not in HBNBCommand.allowed_classes:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                all_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                all_list.append(str(value))

        print(all_list)

    def do_update(self, arg):
        new = arg.partition(" ")
        cl_name = new[0]
        cl_id = new[2]
        cl_attr = new[4]
        cl_attr_value = new[6]
        
        if not cl_name:
            print("** class name missing **")
            return
        
        if cl_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return
        
        if not cl_id:
            print("** instance id missing **")
            
        if not cl_attr:
            print("** attribute name missing **")
            return
        
        if not cl_attr_value:
            print("** value missing **")
            return
        
        if cl_attr:
            setattr(self, cl_attr, str(cl_attr_value))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
