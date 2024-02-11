#!/usr/bin/python3
import models 
from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        
        if kwargs:
            datetime_object = None
            for keys, values in kwargs.items():
                if keys in ["updated_at", "created_at"]:
                    if type(values) is str:
                        datetime_object = datetime.strptime(values, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, keys, datetime_object)
                    else:
                        setattr(self, keys, datetime_object)
            setattr(self, 'id', kwargs.get('id', str(uuid4())))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):

        exclude = ["my_number", "name"]
        my_dictionary = {}
        for keys, values in self.__dict__.items():
            if keys not in exclude:
                my_dictionary[keys] = values

        my_dictionary["__class__"] = self.__class__.__name__

        return dict(my_dictionary)
    

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()


    def __str__(self):
        class_name = self.__class__.__name__

        return f"[{class_name}] ({self.id}) {self.__dict__}"
