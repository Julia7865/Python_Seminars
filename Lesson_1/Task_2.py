# Напишите программу, которая на вход принимает 5 чисел и
# находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90


# a, b, c, d, e = int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: ')),
# max = 0
# if a > max:
#     max = a
# if b > max:
#     max = b
# if c > max:
#     max = c
# if d > max:
#     max = d
# if e > max:
#     max = e
# print(f'Максимальное число -> {max}')


numbers = []
for i in range(1, 6):
    numbers.append(int(input(f'Введите числа {i} число: ')))
max = numbers[0]
for j in range(5):
    if numbers[j] > max:
        max = numbers[j]
print(f'Максимальное число -> {max}')





























