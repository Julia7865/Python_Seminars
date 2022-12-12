# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.

# *Пример:*

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


my_list = [1, 5, 2, 3, 4, 6, 1, 7] 
print(my_list)
find = int(input('Введите стартовый элемент: '))
index = 0
for i, item in enumerate(my_list):
    if item == find:
        index = i
        break

def create_list(sm_list: list):
    element = sm_list[0]
    special_list = [sm_list[0]]
    for i in range(1, len(sm_list)):
        if sm_list[i] - 1 == element:
            special_list.append(sm_list[i])
            element = sm_list[i]
    return special_list

new_list = my_list[index:]

print(create_list(new_list))

        