#!/usr/bin/python3
""" Base class of all other classes in this project"""
import json


class Base:
    """ first class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        my_list = []
        fname = cls.__name__ + '.json'
        if (list_objs is None):
            with open(fname, 'w') as f:
                f.write(my_list)
        for ins in list_objs:
            my_list.append(ins.to_dictionary())
        jstr = cls.to_json_string(my_list)
        with open(fname, 'w') as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if (json_string is None or len(json_string) == 0):
            return ("[]")
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if (cls.__name__ == 'Rectangle'):
            dummy = cls(1, 2)
        elif (cls.__name__ == 'Square'):
            dummy = cls(3)
        dummy.update(**dictionary)
        return (dummy)
