#!/usr/bin/python3

"""
this file include the BaseModel that we will make other classes in herit from it
they will inherit the attributes and methodes.
"""


import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the Base class that caoitan methodes to be shared and inherite from it"""

    def __init__(self, *args, **kwargs):
        """Initializes public instance attributes."""
        if kwargs:
            datetime_object = None
            for keys, values in kwargs.items():
                if keys in ["updated_at", "created_at"]:
                    if type(values) is str:
                        datetime_object = datetime.strptime(
                            values, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, keys, datetime_object)
                    else:
                        setattr(self, keys, datetime_object)
            setattr(self, 'id', kwargs.get('id', str(uuid4())))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def to_dict(self):
        """Returns a dictionary representation of the class for JSON serialization."""

        my_dictionary = {"__class__": self.__class__.__name__}
        for keys, values in self.__dict__.items():
            if type(values) is not datetime:
                my_dictionary[keys] = values
            else:
                my_dictionary[keys] = values.isoformat()

        return dict(my_dictionary)

    def save(self):
        """Updates the 'updated_at' attribute to the current datetime and saves changes."""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Returns a string representation of the class and its attributes."""
        class_name = self.__class__.__name__

        return f"[{class_name}] ({self.id}) {self.__dict__}"


