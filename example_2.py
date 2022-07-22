# Заданиие 2:
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
n = int(input ('Введите количество чисел в списке n: '))
my_list =[]
for i in range(0, n):
    t = random.randint(0, 9)
    my_list.append(t)
print(my_list)

multi = []
i = 0
index = n-1
multiplication = 1
while i <= index :
        multiplication = my_list[i] * my_list[index]
        multi.append(multiplication)
        index -=1
        i+=1
print(f'Произведение пар чисел списка равно: {multi}')