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
    Класс label для формы
    
    Использует Label из tkinter|tk, отвечает за текст и визуал метки
    '''
    def __init__(self):
        self._text = p_w.tk.StringVar() #Используется для дальнейшего изменения текста метки
        self._text.set('Console enable (<>__<>)')
        self._label = p_w.tk.Label(p_w.p_window, 
                             bg='black',
                             foreground='green',
                             anchor='w',
                             font = 'Garamond', textvariable=self._text)
    def changeText(self,E_text):
        self._text.set(E_text)


#Определение метки для вывода данных программы
console = Label()
console._label.place(x=0,y=740,width=1402+p_w.w, height=30)

    
def main():
    while True:
        #Обновление данных окна программы
        p_w.p_window.update_idletasks()
        p_w.p_window.update()
        time.sleep(0.01)

try:
    main()
except p_w.tk.TclError:
    print('Окно было закрыто.')