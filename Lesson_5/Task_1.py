# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие 
# A[i] - 1 = A[i-1]. 
# Найдите это число.

with open('filenumber.txt', 'r') as file:
    my_string = file.readline()

my_list = list(map(int, my_string.split()))
print(my_list)
def find_number(sm_list: list) -> int:
    for i in range(1, len(sm_list)):
        if sm_list[i] - 1 != sm_list[i - 1]:
            return sm_list[i] - 1

out_number = find_number(my_list)
print(out_number)
