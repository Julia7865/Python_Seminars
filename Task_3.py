# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

string1 = input('Введите текст: ')
string2 = input('Введите, что нужно найти в тексте:')
count = 0
for i in range(len(string1)):
    if string2.lower() == string1[i : i + len(string2)].lower():
        count += 1
print(count)

count = string1.count(string2)
print(f'Подстока {string2} встречается в строке '
        f' {string1} {count} раз')