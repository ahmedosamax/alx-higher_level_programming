#!/usr/bin/python3
''' Module for _is_same_class method. '''


def inherits_from(obj, a_class):
    ''' Determine if an object is true subclass of a class'''
    return isinstance(obj, a_class) and type(obj) != a_class
