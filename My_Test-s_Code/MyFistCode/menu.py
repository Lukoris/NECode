"""--------------------------------------------------------
Задача 1 составление меню блюд

Работа со словарём
----------------------------------------------------------
"""
__all__ = ['main']
__version__ = '0.1'


if __name__ != '__main__':
    print('Добавлен модуль Menu')
    print(__version__)
else:
    pass



#Переменные
k=0
b=0
choice_menu = ''
menu_do = dict()
menu = ('Menu:\n\
breakfast:\n\
    1-eggs\n\
    2-eggs with beacon\n\
    3-wuffels\n\
    4-fruits\n\
dinner:\n\
    5-soup\n\
    6-roast potatos\n\
    7-macarela\n\
    8-meat\n\
    9-fish\n\
dessert:\n\
    10-cupcake\n\
    11-cake\n\
    12-cokkie\'s\n\
    13-supercake\n\
wine:\n\
    14-white apple\n\
    15-black strawberry\n\
    16-cherry love')


def main():
    #Переменные
    global k, b, choice_menu, menu_do, menu
    
    #Вывод меню для просмотра пользователем
    print('Welcome to the Rome cafe.\n', menu)
    
    
    #Преобразование в список со строками Меню, отсеив лишнее
    menu = list(menu.split('    '))
    menu = list((''.join(menu)).split('\n'))
    
    
    #Разбитие текстового menu на словарь    
    for i in range(len(menu)):
        'получаем индекс для обращения к menu'
        #Переменные для поиска блюд по их номеру
        first_num=''
        second_num=''
        end_num=''
        for char in menu[i]:           
            'получаем символ элемента'
            
            if char == '-':
                'Ищем разделитель между номером и блюдом'
                
                if k == 1:
                    end_num = second_num
                    
                else:
                    end_num = first_num+second_num
                menu_do[int(end_num)] = menu[i]
                end_num=''
                second_num=''
                first_num=''
                k=0
                
            #Является ли наш символ числом    
            elif char.isdigit():
                k+=1 #Счётчик, что бы контролировать двузначность числа
                second_num = char
                
                if k == 1:
                    'Число возможно двузначное'
                    first_num = second_num
                    
                else:
                    k = 0 #Число однозначное
                    
            else:
                pass
            
            
    #Получение заказа    
    print('Введите номера ваших заказов через пробел:')
    choice_menu = list(set(input(choice_menu).split(' '))) #Отсеивание дубликатов при помощи set() 
    
    
    #Обработка заказа
    for i in range(len(choice_menu)):
        'Преобразование элементов последовательности списка в тип int'
        choice_menu[i] = int(choice_menu[i])
    choice_menu.sort() #Сортировка последовательности
        
        
    #Вывод названия блюд из заказа
    print('Ваш заказ: ')
    for k in range(len(choice_menu)):
        'получаем число элементов для итерации заказов пользователя'
        
        for b in menu_do.keys():
            'получаем ключ для поиска блюда'
            
            if choice_menu[k] == b:
                print(menu_do[b])
                
            else:
                pass
