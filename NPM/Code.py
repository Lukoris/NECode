"""
Only TXT file's'
"""
import os
import random
    
class open_file():
    '''
    Used to open a file.
    
    Opportunities: _read, _write, _append 
    '''
    
    def __init__(self,name):
        self.name = name
        
    def _read(self):
        self.text = open(self.name,'rt')
    def _write(self):
        self.text = open(self.name, 'wt')
    def _append(self):
        self.text = open(self.name, 'at')


class file_operation(open_file):
    '''
    Used for actions with a file and its contents.
    
    Opportunities: _close, _copy
    __str__ Used for text output.
    '''
    def _close(self):
        self.text.close()
        
    def __str__(self):
        print('Opening file.\n')
        self._read()
        print('File name: ', self.name)
        print('File mode: ', self.text.mode)
        return self.text.read()
    
    def _copy(self):
       self._read()
       self.copy = self.text.readlines()
       self._close()
       return self.copy
        
#Not end
class file_writing(open_file):
    '''
    For write text in file
    '''
    def _openwrite(self):
        User_text = ''
        print("You're open file: ", self.name)
        self._write()
        print("Enter you're text: "); User_text = input()
        self.text = User_text
        self.text.close()
#        

def Formatting_copy(file):
    '''
    Formats the contents of the copied file.
    
    Formats a list of lines from a file into a line for text output.
    '''
    file = ''.join(file)
    return file

directory = os.listdir()
file_name = ''

def main():   
    global file_name, file
    
    print('Enter you\'re file name: ', end='')
    file_name = input()+'.txt'
    
    #File variable
    if file_name in directory:
            file = file_operation(file_name)
    else:
        while True:
            #Not found file
            print('File not found\nCreate new file?  Y/N')
            choice = input()
        
            #Create New
            if choice.lower() == 'y':
                file = file_operation(file_name)
                file._write()
                file._copy()
                print('New File append')      
            #Cancel
            elif choice.lower() == 'n':
                print('Canceled creating new file')
                break
            #Unknown input
            else: 
                print('Input you\'re choice again')
    
#Now don't used
def matrix_generator(i,j):
    '''
    Matrix Generator
    
    matrix_generator(i,j) A list generator is used. 
    Main generator [[receiving operation] structure creation] 
    The receiving operation: generates a list of column values. 
    Creating a structure: receives a column and embeds it into a row.
    '''
    
    matrix = [[random.randint(0,100) for _n in range(j)] \
              for _n in range(i)]
    
    return matrix


main()
print(file)
file._close()
file_texti = file._copy()
file_texti = Formatting_copy(file_texti)
print(file_texti.text)