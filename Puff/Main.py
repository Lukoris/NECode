# -*- coding: utf-8 -*-
"""
(─‿‿─)

@author: lukoris
"""

__version__ = '0.1'


#Импорты
from Package import program_window as p_w
import time


class Label():
    '''
    The label class for the form
    
    Uses Label from tkinter|tk, responsible for label text and visual
    '''
    def __init__(self):
        self._text = p_w.tk.StringVar() #Used to permanently change the label text.
        self._text.set('Console enable (<>__<>)')
        self._label = p_w.tk.Label(p_w.p_window, 
                             bg='black',
                             foreground='green',
                             anchor='w',
                             font = 'Garamond', textvariable=self._text)
    def changeText(self,E_text):
        self._text.set(E_text)


#Defining a Label for Program Data Output.
console = Label()
console._label.place(x=0,y=740,width=1402+p_w.w, height=30)

    
def main():
    while True:
        #Updating program window data.
        p_w.p_window.update_idletasks()
        p_w.p_window.update()
        time.sleep(0.01)

try:
    main()
except p_w.tk.TclError:
    print('The window was closed.')
