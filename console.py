#!/usr/bin/python3
""""""

import cmd
import sys
from datetime import datetime
from models.basemodel import BaseModel
from models.Blog import Blog
from models.Chosen_path import ChosenPath
from models.Comments import Comments
from models.Comment_likes import CommentLikes
from models.Likes import Likes
from models.Requests import Requests
from models.Response import Response
from models.Role import Role
from models.sign import SignUp
from models.Specialization import Specialization
from models.Student_points import StudentPoints
from models.__init__ import storage
import shlex

classes = {"Comments": Comments, "Blog": Blog,
        "ChosenPath": ChosenPath, "BaseModel": BaseModel, 
        "Likes": Likes, "Response": Response, 
        "Requests": Requests, "CommentsLikes": CommentLikes, 
        "Role": Role, "SignUp": SignUp, 
        "Specialization": Specialization, 
        "StudentPoints": StudentPoints
        }

class HBNBCommand(cmd.Cmd):
    """"""

    prompt = '(mentConnect)$ '

    def do_EOF(self, arg):
        """exists how much"""
        return True

    def do_quit(self, arg):
        """exists how much"""
        return True

    def emptyline(self):
        """"""
        pass

    def k_v_parser(self, args):
        """"""

        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """"""

        try:
            arg = arg.split()
            if len(arg) < 1:
                print("** class name missing **")
                return False
            if arg[0] in classes:
                new_dict = self.k_v_parser(arg[1:])
                instance = classes[arg[0]](**new_dict)
                del (instance._sa_instance_state)
                print(instance)
            else:
                print("** class doesn't exist **")
                return False
            print(instance.id)
            instance.save()
        except Exception as e:
            print(f"Error: {e}")

    def do_show(self, arg):
        """show the class"""

        arg = arg.split()

        if len(arg) < 1:
            print("** class name missing **")
            return
        class_name = arg[0]
        if class_name not in globals():
            print("** class doesn't exist **")
        if len(arg) < 2:
            print("** instance id missing **")
            return

        instance_id = arg[1]

        key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(key)

        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """destroy the class"""

        arg = arg.split()

        if len(arg) < 1:
            print("** class name missing **")
            return
        class_name = arg[0]
        if class_name not in globals():
            print("** class doesn't exist **")
        if len(arg) < 2:
            print("** instance id missing **")
        instance_id = arg[1]

        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            storage.all().pop(key)
            storage.save()

    def do_all(self, arg):
        """alll the class"""

        args = shlex.split(arg)
        objlist = []
        
        try:
            if len(args) == 0:
                objdict = storage.all()
            elif args[0] in classes:
                objdict = storage.all(classes[args[0]])
            else:
                print("** class doesn't exist **")
                return False
            for key in objdict:
                objlist.append(str(objdict[key]))
                print(objlist)
            print("[", end="")
            print(", ".join(objlist), end="")
            print("]")
        except Exception as e:
            print(f"Error: {e}")
    def do_update(self, arg):
        """update the cl;ass"""

        arg = arg.split()

        if len(arg) < 1:
            print("** class name missing **")
            return

        class_name = arg[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        instance_id = arg[1]
        key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return

        if len(arg) < 3:
            print("** attribute name missing **")
            return

        attribute_name = arg[2]

        if len(arg) < 4:
            print("** value missing **")
            return

        attribute_value = arg[3]

        if len(arg) > 4:
            return

        if attribute_name == "id" or attribute_name == "created_at" or attribute_name == "updated_at":
                return
        #attribute_value = type(getattr(instance, attribute_name))(attribute_value)
        try:
            instance[attribute_name] = attribute_value
            storage.save()
        except (AttributeError, ValueError) as e:
            print(f"Error updating attribute: {e}")


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except Exception as e:
        print(f"Error: {e}")
