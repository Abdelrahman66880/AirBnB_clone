#!/usr/bin/python3

"""
This is the interpreter that accept commands that can be use to use
and manpulate the  objects and doing with several function.
"""
import re
import cmd
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models.City import City
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
    
    def handle_custom_command(self, class_name, action):
        """Handle custom commands like <class name>.all()
        or <class name>.count()."""
        chips = action.split("(")
        if len(chips) == 2 and chips[1].endswith(')'):
            action_name = chips[0]
            action_args = chips[1][:-1].split(',')

            # Edit
            action_args = [arg.strip('\"') for arg in action_args]

            if action_name == 'show':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print(f"** no instance found **")
            elif action_name == 'all':
                objects = [
                    str(obj) for key, obj in storage.all().items()
                    if key.startswith(class_name + '.')
                ]
                print(objects)
            elif action_name == 'count':
                count = sum(
                    1 for key in storage.all()
                    if key.startswith(class_name + '.')
                )
                print(count)
            elif action_name == 'destroy':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print(f"** no instance found **")
            elif action_name == 'update':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    obj = storage.all()[key]
                    attribute_name = action_args[1]
                    attribute_value = action_args[2]
                    setattr(obj, attribute_name, attribute_value)  # Editing the attributes with the given values
                    obj.save()
                else:
                    print(f"** no instance found **")
            else:
                print(f"Unrecognized action: {action_name}.\
                Type 'help' for assistance.\n")
        else:
            print(f"Unrecognized action: {action}.\
            Type 'help' for assistance.\n")

    def default(self, line):
        """Handle unrecognized commands."""
        chips = line.split('.')
        if len(chips) == 2:
            class_name, action = chips
            self.handle_custom_command(class_name, action)
        else:
            print(f"Unrecognized command: {line}.\
                  Type 'help' for assistance.\n")


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
            return



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
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        chips = line.split()

        if not chips:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s(".*"|[^"]\S*)?)?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** invalid command format **")
            return

        classname, uid, attribute, value = match.groups()

        if classname not in self.classes:
            print("** class doesn't exist **")
            return
        elif not uid:
            print("** instance id missing **")
            return

        key = f"{classname}.{uid}"
        if key not in storage.all():
            print("** no instance found **")
            return
        elif not attribute:
            print("** attribute name missing **")
            return
        elif not value:
            print("** value missing **")
            return

        obj = storage.all()[key]
        setattr(obj, attribute, value)
        storage.all()[key].save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

