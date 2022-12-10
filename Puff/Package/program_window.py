'''
Program window
'''

import tkinter as tk
from PIL import Image, ImageTk


__version__ = '0.1'

if __name__ != '__main__':
    print('Importing a module...', __name__)



#Program window.
p_window = tk.Tk()


#Screen size options.
w = p_window.winfo_screenwidth()
h = p_window.winfo_screenheight()
#Finding the middle of the parameter.
w = w//2
h = h//2 
#Selection by screen resolution.
if w == 960:
    w = w - 800 #Offset from the middle.
    h = h - 400
else:
    pass
    '''
    Other permissions not provided.
    '''
    
    
#Configuring the program window.
p_window.title('Puff')  
p_window.geometry('1402x800+{0}+{1}'.format(w,h))
p_window.resizable(width=False, height=False)
p_window.configure(bg='black')

try:
    image = Image.open('redheadandwolf.png')
except:
    print('An image for the background of the program was not found.')
else:
    #Assigning the background of the program.
    background_image = ImageTk.PhotoImage(image, master=p_window)
    background = tk.Label(p_window, image = background_image)
    background.image = image
    background.grid(row=0, column=0)
    
