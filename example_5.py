# Задача 5:
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('Введите количество чисел K: '))
fibo = [1, 1]
nega = [1, -1]

for i in range(2, k):
    f = fibo[i-1] + fibo[i-2]
    fibo.append(f)
    n = nega[i-2] - nega[i-1]
    nega.append(n)

nega.reverse()
nega.append(0)
print(f' для k = {k} ==> {nega + fibo}')