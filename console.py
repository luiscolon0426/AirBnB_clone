#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd
from typing import KeysView
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

    def default(self, arg):
        """ In case command starts with <class name>.<method name>() 
        """
        sep_arg = arg.split('.')
        if len(sep_arg) < 2:
            print("*** Unknown Syntax,", arg)
            return
        else:
            if sep_arg[0] in HBNBCommand.allowed_classes:
                if sep_arg[1] == "count()":
                    self.do_count(sep_arg[0])
                elif sep_arg[1] == "all()":
                    self.do_class_name_all(sep_arg[0])


    def do_quit(self, arg):
        """
        exit the programm with:
        - quit
        - EOF
        - Ctrl-D
        """
        return True

    def do_EOF(self, arg):
        """
        exit the programm with:
        - quit
        - EOF
        - Ctrl-D
        """
        return True

    def emptyline(self):
        """
        empty line + Enter should
        not print/execute anything
        """
        return False

    def do_create(self, arg):
        """
        creates instance of allowed_classes
        save it to json and prints the id
        """
        if len(arg) == 0:
            print("** class name missing **")

        elif arg:
            create_dic = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review
            }
            for key, value in create_dic.items():
                if arg == key:
                    new = create_dic[arg]()
                    print(new.id)
                    storage.new(new)
                    storage.save()
                    return
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """
        prints the string rep of an instance
        based on the class method
        """
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
        """
        Deletes an instance specified by the user
        and save the changes to JSON file
        """
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
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        prints all the string rep of instance based or not in the class name
        """
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

    def do_class_name_all(self, arg):
        """
        prints all instances of a class by using:
        <class name>.all()
        """
        exclusive_class_list = []
        for key, value in storage._FileStorage__objects.items():
            if arg in key:
                exclusive_class_list.append(str(value))
        print(exclusive_class_list)


    def do_update(self, arg):
        """
        Updates an instance based or not in the class name
        """
        new = arg.partition(" ")
        cl_name = new[0]
        cl_id = new[2]
        sep_id_further = cl_id.partition(" ")
        cl_id = sep_id_further[0]
        sep_email = sep_id_further[2].partition(" ")
        cl_attr = sep_email[0]
        cl_attr_value = sep_email[2]

        if not cl_name:
            print("** class name missing **")
            return

        if cl_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return

        if not cl_id:
            print("** instance id missing **")
            return

        if cl_id:
            cl_name = cl_name + "." + cl_id
            if cl_name not in storage.all().keys():
                print("** no instance found **")
                return

        if not cl_attr:
            print("** attribute name missing **")
            return

        if not cl_attr_value:
            print("** value missing **")
            return

        if cl_attr:
            setattr(self, cl_attr, str(cl_attr_value))


    def do_count(self, arg):
        """
        Retrieves instances of a class based on his ID:
        <class name>.count()
        """
        if arg in HBNBCommand.allowed_classes:
            mod = storage.all()
            mod_num = 0
            for key in mod.keys():
                if arg in key:
                    mod_num += 1
            print(mod_num)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
