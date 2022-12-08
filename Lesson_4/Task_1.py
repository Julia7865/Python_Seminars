# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

str_list = input('Введите числа через пробел: ').split(' ')
# for i in range(len(str_list)):
#     str_list[i] = int(str_list[i])
print(min(str_list))
print(max(str_list))
