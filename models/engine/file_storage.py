#!/usr/bin/python3
import json
from os.path import exists

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):

        if exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj = globals()[class_name](**value)
                        self.__objects[key] = obj
            except json.JSONDecodeError:
                pass  # Handle the case when the file is empty or not in a valid JSON format

