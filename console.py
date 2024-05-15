#!/usr/bin/python3
"""entry point of the command interpreter"""

from cmd import Cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(Cmd):
    """class for command interpreter"""
    prompt = '(hbnb) '
    models = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print()
        exit()

    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything"""
        pass

    @staticmethod
    def command_check(args):
        # print(args)
        temp = args.partition(" ")
        class_name = temp[0]
        command_id = temp[2].partition(" ")[0]
        args = temp[2].partition(" ")[2]

        # print(temp)
        # print(command_name, command_id)

        if not class_name:
            print("** class name missing **")
            return
        if class_name not in HBNBCommand.models:
            print("** class doesn't exist **")
            return
        if not command_id:
            print("** instance id missing **")
            return
        key = class_name + '.' + command_id
        if key not in storage.all():
            print("** no instance found **")
            return
        return key, args

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) 
        and prints the id.
        """
        if arg in HBNBCommand.models:
            newModel = HBNBCommand.models[arg]()
            storage.save()
            print(newModel.id)
        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance 
        based on the class name and id.
        """
        # print(key)
        if self.command_check(args):
            key = self.command_check(args)[0]
            print(storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if self.command_check(args):
            key = self.command_check(args)[0]
            del storage._FileStorage__objects[key]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of 
        all instances based or not on the class name.
        """
        print_list = []
        if arg:
            class_name = arg.split(' ')[0]
            if class_name not in HBNBCommand.models:
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    if key.split('.')[0] == arg:
                        print_list.append(str(value))
        else:
            for key, value in storage.all().items():
                print_list.append(str(value))
        print(print_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id 
        by adding or updating attribute
        (save the change into the JSON file)
        """
        if self.command_check(args):
            key = self.command_check(args)[0]
            args = self.command_check(args)[1]

            # print(key)
            # print(args)
            # print(key.split("."))
            # print(line)
            # print(len(line))

            temp = args.partition(" ")
            if not temp[0]:
                print("** attribute name missing **")
                return 
            if not temp[2]:
                print("** value missing **")
                return
            
            attr = temp[0]
            second_quote = temp[2].find('\"', 1)
            value = temp[2][1:second_quote]
            
            # print(attr)
            # print(value)

            new_dic = storage.all()[key]
            new_dic.__dict__[attr] = value
            # print(new_dic.__dict__)
            storage.save()

    def do_kill(self, arg):
        storage._FileStorage__objects = {}
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
