#!/usr/bin/python3
"""
This is the interpreter that accept commands that can be use to use
and manpulate the  objects and doing with several function.
"""
import cmd
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    """Simple console using CRUD commands"""

    classes = {
        "User": User,
        "Place": Place,
        "Review": Review,
        "State": State,
        "Amenity": Amenity,
        "City": City,
        "BaseModel": BaseModel
    }

    prompt = "(hbnb) "
    missing_class = "** class name missing **"
    missing_id = "** instance id missing **"
    missing_attr = "** attribute name missing **"
    missing_val = "** value missing **"
    unknown_class = "** class doesn't exist **"
    unknown_id = "** no instance found **"
    not_exist = "** class doesn't exist **"

    def __init__(self):
        super().__init__()
        self.users = {}

    def emptyline(self):
        """Ignore default behavior on an empty line."""
        pass

    def do_quit(self, line):
        "Quit command to exit the program"
        return True
    
    def do_EOF(self, line):
        """Exit with EOF command (Ctrl+D). Usage: Ctrl+D"""
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = line.split(" ")
        if args:
            class_name = args[0]
            if class_name in self.classes:
                new_instance = self.classes[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print(self.unknown_class)
        else:
            print(self.missing_class)



    def do_show(self, line):
        """Prints the string representation of an instance."""
        args = line.split()
        if not args:
            print(self.missing_class)
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print(self.unknown_class)
                return
            if len(args) < 2:
                print(self.missing_id)
            else:
                object_id = args[1]
                key = "{}.{}".format(class_name, object_id)
                objects = storage.all()
                if key in objects:
                    print(objects[key])
                else:
                    print(self.unknown_id)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()
        if not args:
            print(self.missing_class)
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print(self.unknown_class)
                return
            if len(args) < 2:
                print(self.missing_id)
            else:
                object_id = args[1]
                key = "{}.{}".format(class_name, object_id)
                objects = storage.all()
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print(self.unknown_id)

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name."""
        args = line.split()
        if not args:
            objects = storage.all()
            print([str(objects[key]) for key in objects])
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print(self.unknown_class)
                return
            objects = storage.all()
            filtered_objects = [str(objects[key]) for key in objects if key.startswith(class_name + ".")]
            print(filtered_objects)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = line.split()
        if not args:
            print(self.missing_class)
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print(self.unknown_class)
                return
            if len(args) < 2:
                print(self.missing_id)
            else:
                object_id = args[1]
                key = "{}.{}".format(class_name, object_id)
                objects = storage.all()
                if key not in objects:
                    print(self.unknown_id)
                    return
                if len(args) < 3:
                    print(self.missing_attr)
                else:
                    attribute_name = args[2]
                    if len(args) < 4:
                        print(self.missing_val)
                    else:
                        attribute_value = args[3]
                        obj = objects[key]
                        setattr(obj, attribute_name, attribute_value)
                        obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

