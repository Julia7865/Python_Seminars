# Функции

# Принимает, но не возвращает

# c = 0
# def function(a, b):
#     global c
#     c = a + b
# print(c)
# function(3, 4)
# print(c)

# Не принимает, но возврящает(нужно записать стр19)

# import random

# def function(a: int = 10, b: int= 100) -> list:
#     new_list = []
#     for i in range(a):
#         number = random.randint(0, b)
#         new_list.append(number)
#     return new_list

# my_list = function()
# print(my_list)

# Ловит ошибки

# def input_int(text: str, error: str) -> int:
#     while True:
#         try:
#             number = int(input(text))
#             return number
#         except:
#             print(error)

# number = input_int('Введите целое число: ', 'Ошибка! Введите ЦЕЛОЕ число')
# print(number)

# Данные

# my_list = [345, 123, 45, 643, 345]       # список
# my_tuple = (3445, 6757, 456, 67)        # кортеж
# my_set = {34, 564, 34, 43363, 6}        # множество
# my_dict = {1: '-', 2: '!', 3: '+'}           # словарь

# Пройтися по словарю

# for i in my_dict:    # выведет на печать ключи
#     print(i)

# for i in my_dict.values():    # выведет на печать значение
#     print(i)

# for key, value in my_dict.items:    # выведет на печать ключи и их значение
#     print(key)
#     print(value)

# как обртиться к элементу словаря
# print(my_dict[1])   # выведет значние под ключом 1 
# print(my_dict.get(0))  # сделает тоже самое, но в случае ошибки программа не сломается

# Множество. можно добавлять
# my_set.add(456)
# print(my_set)

# Можно найти или проверить есть ли элемент
# find = 56
# if find in my_set:
#     print(True)
# else:
#     print(False)

# for i in my_set:
#     print(i)

# С помощью множества можно очистить список от повторений
# print(my_list)
# my_list = set(my_list)
# my_list = list(my_list)
# print(my_list)

# Кортеж для изменения можно перевести в список
# my_tuple = list(my_tuple)
# my_tuple[2] = 't'
# my_tuple = tuple(my_tuple)
# print(my_tuple)