"""
@author: me :^
"""

__version__ = '0.2'

if __name__ != '__main__':
    print('Добавлен Основной модуль')
    print(__version__)
else:
    pass



#Импортируемые модули
from MyFistCode import doList
from MyFistCode import Registration_user as reg_user


#Переменные
choice_num = ''
q_exit = ''
reg_user.registration()
user = reg_user.user
    
    
#Тело программы   
print('\nДобро пожаловать ',user.name,'!\n')
while q_exit != 'q':
    choice_num = int(doList.write_list())
    
    #Запуск задачи
    if choice_num == 1:
        print('Инициализирую 1-ую задачу...\n')
        doList.menu_start()
            
    elif choice_num == 2:
        print('Инициализирую 2-ую задачу...\n') #Не создана
          
    else:             
        pass
    
    print('Если желаете отменить задачник введите \'q\' ',end='')
    q_exit = input(q_exit)
    
else:
    choice_num = ''
    q_exit = ''

#Справочник
print('Если вам нужна сводка по модулям введите 1-да, 0-нет')
choice_num = int(input(choice_num))

if choice_num == 1:
    print('Out help info \n')
    print('Registration_user: \n', reg_user.__doc__, '\n doList: \n', doList.__doc__,
          '\n menu: \n', doList.menu.__doc__)
    
else:
    print('Exit from program')
