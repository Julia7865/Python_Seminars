# Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

for i in range(1, a* b - 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break

i = 1
while(max(a, b)*i)%min(a, b) != 0:
    i += 1
print(max(a, b)*i)