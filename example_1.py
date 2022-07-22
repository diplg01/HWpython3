# Задание 1:
# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

n = int(input ('Введите количество чисел в списке n: '))
my_list =[]
for i in range(0, n):
    t = random.randint(0, 99)
    my_list.append(t)
print(my_list)

print('На нечетных позиция стоят следующие элементы:', end = ' ')
sum = 0

sum = 0
for i in range (0, n):
    if i % 2 != 0:
        sum += my_list[i]
        print (my_list[i], end = ' ')
print()
print(f'Сумма элементов на нечетных позициях = {sum}')
