#!/usr/bin/python3
'''
A module that contains the console class.
'''
import cmd
import models


class HBNBCommand(cmd.Cmd):
    '''
    A class that sets the airbnb console.
    '''
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''
        A method that quits the console.
        '''
        return True

    def do_EOF(self, arg):
        '''
        The End of file Method.
        '''
        return True

    def emptyline(self):
        '''
        A method for enter prompt to do nothing.
        '''
        pass

    def do_create(self, args):
        if not args:
            print("** class name missing **")
            return
        
        if args not in globals():
            print("** class doesn't exist **")
            return

        cls = globals()[args]
        new_instance = cls()

        models.storage.save()

        return new_instance.id

    def do_show(self):




if __name__ == '__main__':
    HBNBCommand().cmdloop()
