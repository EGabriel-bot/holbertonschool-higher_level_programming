#!/usr/bin/python3
"""Base"""
import json


class Base:
    """Class named Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_onjs):

        if list_onjs is None:
            empty = []
            json.dump(empty, cls)
        with open(cls, "w", encoding="utf-8") as f:
            strrep = cls.to_json_string(list_onjs)
            wrote_data = f.write(strrep)

    def from_json_string(json_string):
        if json_string is None or not json_string:
            empty = []
            return empty
        else:
            return json_string
