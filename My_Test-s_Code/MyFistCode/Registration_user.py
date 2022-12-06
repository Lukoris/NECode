"""-----------------------------------------------------------------
Регистратор и пользователь

Регистрация пользователя и занесение его данных в новый экземпляр, как его свойств.
------------------------------------------------------------------
"""
__all__ = ['registration']
__version__ = '0.1'


if __name__ != '__main__':
    print('Добавлен модуль регистрации')
    print(__version__)
else:
    pass



class people():
    '''
    Отвечает за класс человека
    
    Содержит в себе свойства для экземпляра человека
    '''
    def __init__(self,name):
        #Назначает имя человека
        self.name = name
        
    def height(self,height):
        #Назначает рост человека
        self.height = height
    
    def mass(self,mass):
        #Назначает вес человека
        self.mass = mass
    
    def age(self,age):
        #Назначает возраст человека
        self.age = age
        
    def work(self,work):
        #Назначает работу человека
        self.work = work


user,name,height,mass,age,work = ['']*6



def registration():
    '''
    Регистрация пользователя
    
    Принимает введённые аргументы от пользователя и присваивает их к свойствам объекта
    '''
    #Переменные
    global user,name,height,mass,age,work
    args = ['name','height','mass','age','work']
    
    #Цикл для ввода данных
    for number in range(len(args)):
        print('Введите {0}: '.format(args[number]),end='')
        args[number] = input()
        
    #Назначение свойств для экземпляра человека
    user = people(args[0])
    user.height = args[1]
    user.mass = args[2]
    user.age = args[3]
    user.work = args[4]
