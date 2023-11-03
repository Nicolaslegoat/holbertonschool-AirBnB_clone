#!/usr/bin/python3
'''
A module that contains the console class.
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    A class that sets the airbnb console.
    '''
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''
        A method that quit the console.
        '''
        return True

    def do_help(self, arg):
        '''
        The method to print helping message.
        '''
        print("Quit command to exit the program")

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
