# -*- coding: utf-8 -*-
"""
13.12.22

@author: Lukoris
"""

__version__ = '0.1'
__author__ = 'Lukoris'


def display_info(cls):
    """Used to output docstring's of class methods.

Argument - Class
    """
    method_list = [method for method in dir(cls)
                   if callable(getattr(cls, method))
                   and method.startswith('__') is False]

    for method in method_list:
        method_doc = getattr(cls, method).__doc__
        print('"' + method + '"')

        if method_doc is None:
            print('This method does not have docstring.\n')
        else:
            print('This is the docstring:\n',
                  method_doc)


def main():
    pass
