"""---------------------------------------------------------------------
Задачник

Хранит и инициализирует заданные задачи
-----------------------------------------------------------------------
"""

__all__ = ['write_list','menu_start']
__version__ = '0.1'


if __name__ != '__main__':
    print('Добавлен модуль задачника')
    print(__version__)
else:
    pass



#Модули
from MyFistCode import menu

#Функции
def write_list():
    'Выводит список задач'
    print('''Список возможных задач:
              1. Заполнение дневного рациона
              2. Планы на день
                  
Введите номер задачи: ''', end='')
    return input()
def menu_start():
    menu.main()
