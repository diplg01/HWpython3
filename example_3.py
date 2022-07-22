# Задание 3:
# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


n = int(input('Введите количество чисел в списке N = '))
my_list =[]
for i in range(0, n):
    temp = float(input(f'Введите число {i} = '))
    my_list.append(temp)

print(my_list, end =' => ')
new = []
point = 0
for i in my_list:
    temp = i - int(i)
    if temp != 0 :
        new.append(temp)
    if str(i)[::-1].find('.') > point:
        point = str(i)[::-1].find('.')
max = abs(new[0])
min = abs(new[0])
for i in new:
    if abs(i) > max:
        max = abs(i)
    if abs(i) < min:
        min = abs(i)
print(round(max - min, point))