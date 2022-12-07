# Задайте список. Напишите программу, 
# которая определит,
# присутствует ли в заданном списке строк некое число.

my_list = ['hdkufdiufn345', '3658djbfyfi', 'sdjh458thri458y']
number = (input('Введите искомый символ: '))
trigger = True
for item in my_list:
    for char in item:
        if char == number:
            print(f'Символ {number} есть в строке {item}')
            trigger = False
            break
if trigger:
    print(f'Символ {number} нет в заданном списке')

for item in my_list:
    for char in item:
        if char == number:
            print(f'Символ {number} есть в строке {item}')
            break
    else:
        print(f'Символа {number} нет в строке {item}')