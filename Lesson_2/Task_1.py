# Напишите программу, 
# которая принимает на вход число N и 
# выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81


number = int(input('Введите число: '))

for i in range(number):
    print((-3) ** i, end=', ')

step = 1
for i in range(number):
    print(step, end=' ')
    step*= -3

my_list = [1]
for i in range(number - 1):
    my_list.append(my_list[i] * -3)
print(*my_list, sep=', ')


my_list2 = []
for i in range(number):
    my_list2.append((-3) ** i)
print(*my_list2, sep=', ')