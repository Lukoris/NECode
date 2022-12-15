# -*- coding: utf-8 -*-
"""Responsible for working on the file.
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


import program_paths as fpath


# Paths
GENERAL_PATH = fpath.formatting_path(__file__, 'general')
DATA_PATH = fpath.formatting_path(__file__, 'data')


class TxtFile:
    """Responsible for the file.

Creates objects that store the text of a '.txt' file
    """

    file_count = 0

    @staticmethod
    def question():
        """Call question() for info
        """

        print("""If you need:
open '.txt' file for read, use .open_file
write a '.txt' file, use .write_file
append text to '.txt' file, use .append_file
File method's:
    open_file
    close_file
    show_text""")

    @classmethod
    def kids(cls):
        """Counts the number of open files.

Variable keeper - file_count
        """
        print('I have', cls.file_count, 'file')

    def __init__(self):
        self.__file_name = None
        self.__file_path = None
        self.status = 'Not found'

        TxtFile.file_count += 1

    @property
    def name(self):
        if self.__file_name is None:
            print('You didn\'t enter a file name.\n')
        else:
            return self.__file_name

    @name.setter
    def name(self, name):
        if self.__file_name is not None:
            print('The file already has the specified name.\n')
        else:
            if self.__file_path is not None:
                if fpath.search_file(self.__file_path, name + '.txt') is True:
                    self.__file_name = name + '.txt'
                    print(f'File: {self.name} - was found.\n')

                    self.status = 'Found'
            else:
                print('You did not specify the path to the',
                      'directory with the file.\n')

    @property
    def path(self):
        if self.__file_path is None:
            print('Path not specified.\n')
            fpath.display_catalog(DATA_PATH)
        else:
            return self.__file_path

    @path.setter
    def path(self, path):
        if self.__file_path is not None:
            print('The file already has the specified path.\n')
        else:
            self.__file_path = DATA_PATH + '\\' + path

    def open_file(self, method='read'):
        """Responsible for opening a file.

Takes 3 arguments: read, write, append
Equal: rt, wt, at
        """

        if self.status == 'Open':
            print(f'File:{self.name} is already open')
        else:
            if self.status == 'Found':
                finally_path = self.path + '\\' + self.name

                if method == 'read':
                    self.file = open(finally_path, 'rt')
                    print('File opened for reading.\n')
                if method == 'write':
                    self.file = open(finally_path, 'wt')
                    print('File opened for writing.\n')
                if method == 'append':
                    self.file = open(finally_path, 'at')
                    print('File is open for adding.\n')

                self.status = 'Open'

            else:
                print('You didn\'t provide a filename or path.\n')

    def close_file(self):
        """Responsible for closing the file
        """

        if self.status == 'Open':
            self.file.close()
            print('File closed.\n')

            self.status = 'Closed'

        else:
            if self.status == 'Not found':
                print('File not found.\n')
            else:
                print('File already closed.\n')

    def show_text(self, method=None):
        if self.status == 'Open':
            line_text = self.file.readline()

            print('File text', self.name)

            while line_text:
                print(line_text)
                line_text = self.file.readline()
            else:
                print('\nReading complete\n')

            if method == 'close':
                self.close_file()

        else:
            print('File not open.\n')

    def __str__(self):
        return ('File name: {} \nPath: {} \nStatus: {} \n'.format(
            self.name,
            self.path,
            self.status))


def debug_code():
    file1 = TxtFile()
    file1.path = 'Test1'
    file1.name = 'test'
    print(file1)


debug_code()
