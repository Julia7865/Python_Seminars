### List Comprehension

import random

# def rand_letter():
#     x = random.randint(0, 10)
#     if x%2 == 0:
#         return 'A'
#     else:
#         return 'b'

# my_list = [x for x in range(10) if x%2 == 0 and x > 0]

# print(my_list)


### MAP(деформирует, меняет  тип,применяет функцию к каждому элементу)

# def rand_letter():
#     x = random.randint(0, 10)
#     if x%2 == 0:
#         return 123
#     else:
#         return 321

# def degree(x):
#     return x**2

# my_list = [rand_letter() for _ in range(-10, 10)]
# print(my_list)
# my_list = list(map(degree, my_list))
# print(my_list)


### FILTER(отсеивает, применяет функцию к каждому элементу)

# def rand_letter():
#     x = random.randint(0, 10)
#     if x%2 == 0:
#         return 5
#     else:
#         return 10

# def degree(x):
#     if x%2 == 0:
#         return x

# my_list = [rand_letter() for _ in range(-10, 10)]
# print(my_list)
# my_list = list(filter(degree, my_list))
# print(my_list)


### ENUMERATE

# def rand_letter():
#     x = random.randint(0, 10)
#     if x%2 == 0:
#         return 'A'
#     else:
#         return 'B'

# def degree(x):
#     if x%2 == 0:
#         return x

# my_list = [rand_letter() for _ in range(15)]
# print(my_list)

# for i, item in enumerate(my_list):
#     if item == "A":
#         print(i)

### ZIP(складывает по элементам)

# def rand_letter():
#     x = random.randint(0, 10)
#     if x%2 == 0:
#         return 'A'
#     else:
#         return 'B'

# def degree(x):
#     if x%2 == 0:
#         return x

# first_list = [rand_letter() for _ in range(15)]
# second_list = [rand_letter() for _ in range(10)]
# third_list = [rand_letter() for _ in range(5)]
# print(first_list)
# print(second_list)
# print(third_list)
# all_list = list(zip(first_list, second_list, third_list))
# print(all_list)


### LAMBDA (функция которую не надо обьявлять)

def rand_letter():
    x = random.randint(0, 10)
    if x%2 == 0:
        return 'A'
    else:
        return 'B'

def degree(x):
    if x%2 == 0:
        return x

my_list = [x for x in range(10)]

my_list = list(map(lambda x: x**2 , my_list))
print(my_list)

command = lambda x: degree(x)