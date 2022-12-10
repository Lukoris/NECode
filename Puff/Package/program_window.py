'''
Program window
'''

import tkinter as tk
from PIL import Image, ImageTk


__version__ = '0.1'

if __name__ != '__main__':
    print('Импортирую модуль', __name__)



#Окно программы
p_window = tk.Tk()


#Параметры размеров экрана
w = p_window.winfo_screenwidth()
h = p_window.winfo_screenheight()
#Нахождение середины параметра
w = w//2
h = h//2 
#Подбор по разрешению экрана
if w == 960:
    w = w - 800 # смещение от середины
    h = h - 400
else:
    pass
    '''
    Другие разрешения, не предусмотренны
    '''
    
    
#Настройка окна программы
p_window.title('Agnis')  
p_window.geometry('1402x800+{0}+{1}'.format(w,h))
p_window.resizable(width=False, height=False)
p_window.configure(bg='black')

try:
    image = Image.open('redheadandwolf.png')
except:
    print('Изображение для фона программы, не было найдено.')
else:
    #Назначение фона программы
    background_image = ImageTk.PhotoImage(image, master=p_window)
    background = tk.Label(p_window, image = background_image)
    background.image = image
    background.grid(row=0, column=0)
    
