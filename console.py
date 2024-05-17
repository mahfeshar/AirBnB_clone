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

    def precmd(self, line: str) -> str:
        """This method is called after the line has been input"""

        # Error: User.all()User.count()

        if not ('.' in line and '(' in line and ')' in line):
            return line

        # Declare command line variables
        _command = _class = _id = _arg = ''
        line_split = line.split('.')
        first_paren = line_split[1].find('(')
        second_paren = line_split[1].find(')')

        # Command
        _command = line_split[1][:first_paren]

        # Class Name
        _class = line_split[0]

        # Between parentheses
        between_parentheses = line_split[1][first_paren+1:second_paren]
        if ', ' in between_parentheses:
            if not ('{' in between_parentheses and '}' in between_parentheses):
                between_list = between_parentheses.split(', ')
                _id = between_list[0][1:-1]
                _arg = between_list[1][1:-1].strip()
                _arg += ' ' + between_list[2].strip()

            else:
                # id dictionary
                between_list = between_parentheses.split(', ', 1)
                _id = between_list[0][1:-1]
                _arg = between_list[1]

        elif between_parentheses != '':
            # id only
            _id = between_parentheses[1:-1]

        line = ' '.join([_command, _class, _id, _arg]).strip()
        return line

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def help_quit(self):
        """ """
        print("Quit command to exit the program")
        print()

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print()
        exit()

    def help_EOF(self):
        """ """
        print("EOF to exit the program\n")

    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything"""
        pass

    @staticmethod
    def command_check(args):
        temp = args.partition(" ")
        class_name = temp[0]
        command_id = temp[2].partition(" ")[0]
        args = temp[2].partition(" ")[2]

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

    def help_create(self):
        """ """
        print("Creates a new instance of BaseModel\n")

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        if self.command_check(args):
            key = self.command_check(args)[0]
            print(storage.all()[key])

    def help_show(self):
        """ """
        print("Prints the string representation of an instance\n")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if self.command_check(args):
            key = self.command_check(args)[0]
            del storage._FileStorage__objects[key]
            storage.save()

    def help_destroy(self):
        """ """
        print("Deletes an instance based on the class name and id\n")

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

    def help_all(self):
        """ """
        print("Prints all string of all instance\n")

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class
        """
        length = 0
        for key, value in storage.all().items():
            if key.split('.')[0] == arg:
                # print(key.split('.')[0])
                length += 1
        print(length)

    def help_count(self):
        """ """
        print("Retrieve the number of instances of a class\n")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)
        """
        if self.command_check(args):
            key = self.command_check(args)[0]
            args = self.command_check(args)[1]

            new_dic = storage._FileStorage__objects[key]

            if not ('{' in args and '}' in args):
                temp = args.partition(" ")

                if not temp[0]:
                    print("** attribute name missing **")
                    return
                if not temp[2]:
                    print("** value missing **")
                    return

                attr = temp[0]

                value = eval(temp[2])
                new_dic.__dict__[attr] = value

            else:
                try:
                    dic = eval(args)
                    for attr, value in dic.items():
                        new_dic.__dict__[attr] = value
                except Exception:
                    pass

            storage.save()

    def help_update(self):
        """ """
        print("Updates an instance based on the class name and id\n")
    # def do_kill(self, arg):
    #     storage._FileStorage__objects = {}
    #     storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
