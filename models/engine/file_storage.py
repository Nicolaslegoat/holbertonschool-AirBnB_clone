#!/usr/bin/python3
'''
A module that contains the Filestorage class.
'''
import json


class FileStorage:
    '''A File storage class.'''
    def __init__(self, file_path, objects):
        self.__file_path = file_path
        self.__objects = objects
