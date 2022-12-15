# -*- coding: utf-8 -*-
"""Responsible for working on the path to the program files.
13.12.22

@author: Lukoris
For Windows
"""

__version__ = '0.1'
__author__ = 'Lukoris'

if __name__ == '__main__':
    print('Started file:', __file__[15:])
else:
    print('Imported module:', __file__[15:])


import os.path
from os import listdir


def formatting_path(path, _type):
    """Formats a directory path.

    type:
        general - main directory.
        data - tag with data.
        module - module directory.
    """
    path = path.split('\\')  # Do list

    if _type == 'general':
        path = tuple(path)[:-2]
        format_path = '\\'.join(path)

    elif _type == 'data':
        path = tuple(path)[:-2]
        format_path = ('\\'.join(path)) + '\\files_with_data'

    elif _type == 'module':
        path = tuple(path)[:-1]
        format_path = '\\'.join(path)

    else:
        print('invalid second argument entered')
        format_path = None

    return format_path


def search_file(path, file_name):
    """Does the file exist?

    Checks the selected directory for a filename.
        The truth will return True
        False will return the string 'File not found'
    """

    if os.path.isfile(path + '\\' + file_name):
        return True
    else:
        print('File not found.')


def display_catalog(main_path):
    """Lists directories in files_with_data and internal files.

    listdir() is used to display the contents of a path.
    'For' iterations are used for pretty output.
    """
    catalogs = listdir(main_path)

    # Catalog's
    for catalog in catalogs:
        files = listdir(main_path + '\\' + catalog)

        print('Catalog:', catalog)

        #  File's
        for file in files:
            print('File:', file)
        print()
