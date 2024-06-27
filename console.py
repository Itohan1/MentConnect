#!/usr/bin/python3
""""""

import cmd
from datetime import datetime
from models.basemodel import BaseModel
from models.Career_path import CareerPath
from models.Blog import Blog
from models.Chosen_path import ChosenPath
from models.Comments import Comments
from models.Comment_likes import CommentLikes
from models.Likes import Likes
from models.Choose_career import ChooseCareer
from models.Requests import Requests
from models.Response import Response
from models.Role import Role
from models.SignUp import SignUp
from models.Specialization import Specialization
from models.Student_points import StudentPoints
from models import storage
import uuid
import os
import shlex

classes = {"CareerPath": CareerPath, "Comments": Comments, "Blog": Blog,
        "ChosenPath": ChosenPath, "ChooseCareer": ChooseCareer, "BaseModel": BaseModel, "Likes": Likes,
        "Response": Response, "Requests": Requests, "CommentsLikes": Comment_Likes, "Role": Role, 
            "SignUp": SignUp, "Specialization": Specialization, "StudentPoints": StudentPoints
            }

class HBNBCommand(cmd.Cmd):
    """"""

    prompt = ('(mentConnect)$ ')

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

        arg = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
            return
        if arg[0] in classes:
            new_dict = self.k_v_parser(arg[1:])
            instance = classes[arg[0]](**new_dict)
            print(instance)
        else:
            print("** class doesn't exist **")
            return
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """"""

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
        """"""

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
        instance = storage.all().get(key)

        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """"""

        arg = shlex.split(arg)
        objlist = []
        
        if len(arg) == 0:
            all_instance = storage.all()
        elif arg[0] in classes:
            objdict = storage.all(classes[arg[0]])
        else:
            print("** class doesn't exist **")
            return
        for key in objdict:
            objlist.append(str(objdict[key]))
        print("[", end="")
        print(", ".join(objlist), end="")
        print("]")
    def do_update(self, arg):
        """"""

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
    HBNBCommand().cmdloop()
