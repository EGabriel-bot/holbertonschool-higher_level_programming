#!/usr/bin/python3
""" Base """
import json


class Base:
    """ Class named Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json method """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_onjs):
        """ save to file method """

        if list_onjs is None:
            empty = []
            json.dump(empty, cls)
        with open(cls, "w", encoding="utf-8") as f:
            strrep = cls.to_json_string(list_onjs)
            wrote_data = f.write(strrep)

    @staticmethod
    def from_json_string(json_string):
        """from json string"""
        if not isinstance(json_string, str) or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
