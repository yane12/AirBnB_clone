#!/usr/bin/python3
""" Module Command Controller entry point """

import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


user_class = {"BaseModel": BaseModel,
              "Amenity": Amenity,
              "City": City,
              "Place": Place,
              "Review": Review,
              "State": State,
              "User": User
              }


class HBNBCommand(cmd.Cmd):
    """ implements the command line interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ quits command line """
        raise SystemExit

    def do_EOF(self, arg):
        """ exits command line """
        raise SystemExit

    def emptyline(self):
        """ handles empty line """
        pass

    def do_create(self, args):
        """ creates a new instance of BaseModel, saves it """
        if len(args) == 0:
            print('** class name missing **')
        elif args in user_class.keys():
            new = user_class[args]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ prints str representation of an instance based on class
        name and id. it splits the argument into a list of strings then checks
        if input is empty, if the first string is a valid class name,
        then if the second string is a valid id, then if the
        concatenated string is in the dictionary of objects, then
        it prints the string representation of the object"""
        list_args = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif list_args[0] in user_class.keys():
            if len(list_args) == 1:
                print("** instance id missing **")
            else:
                obj_search = list_args[0] + "." + list_args[1]
                obj_all = storage.all()
                if obj_search in obj_all:
                    print(str(obj_all[obj_search]))
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """ deletes an instance based on class name and id
        first it splits the argument into a list of strings then checks
        if input is empty, if the first string is a valid class name,
        then if the second string is a valid id, then if the
        concatenated string is in the dictionary of objects, then
        it deletes the object from the dictionary and saves the
        changes to the JSON file"""
        list_args = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif list_args[0] in user_class.keys():
            if len(list_args) == 1:
                print("** instance id missing **")
            else:
                obj_search = list_args[0] + "." + list_args[1]
                obj_all = storage.all()
                if obj_search in obj_all:
                    del obj_all[obj_search]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """ prints str representation of all instances of the object
        it splits the argument into a list of strings then checks
        if input is empty, if the first string is a valid class name,
        then if the concatenated string is in the dictionary of objects,
        then it prints the string representation of the object"""
        if len(args) == 0:
            for key in storage.all():
                print([str(storage.all()[key])])
        elif args not in user_class.keys():
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                key_arg = key.split('.')
                if args == key_arg[0]:
                    print([str(storage.all()[key])])

    def do_update(self, args):
        """ updates an instance based on class name and id
        by adding or updating an attribute
        does this by splitting the argument into a list of strings
        then checks if input is empty, if the first string is a valid
        class name, then if the second string is a valid id, then if
        the concatenated string is in the dictionary of objects,
        then it updates the attribute of the object and saves the
        changes to the JSON file """
        list_args = args.split(" ")
        if len(args) < 1:
            print('** class name missing **')
        if len(list_args) < 2:
            print('** instance id missing **')
        if len(list_args) < 3:
            print('** attribute name missing **')
        if len(list_args) < 4:
            print('** value missing **')
        if list_args[0] not in user_class.keys():
            print("** class doesn't exist **")
        else:
            obj_search = list_args[0] + "." + list_args[1]
            obj_all = storage.all()
            if obj_search in obj_all:
                setattr(obj_all[obj_search], list_args[2],
                        list_args[3].strip('\'"'))
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
