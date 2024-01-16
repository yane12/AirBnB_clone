#!/usr/bin/python3
""" Serializes & deseralizes instances to a JSON file."""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes & deseralizes instances to a JSON file & vice versa."""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """constructor"""
        pass

    @classmethod
    def destroy_all(cls):
        """ Destroys all objects """
        for obj in cls.__objects.values():
            obj.destroy()
        cls.__objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ set in __objects the obj with key <obj class name>.id """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
            dumpy = json.dumps(my_dict)
        with open(self.__file_path, 'w', encoding="UTF8") as f:
            return f.write(dumpy)

    def reload(self):
        """reloads __objects from the JSON file (path: __file_path)"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                obj_dict = json.loads(f.read())
                for key, value in obj_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
