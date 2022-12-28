# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

n = int(input('Input list size: '))

my_list = []

for i in range(n):
    my_list.append(int(input('Input number: ')))
print(f'my list = {my_list}')

new_list = []

for i in range(n):
    if my_list.count(i) == 1:
        new_list.append(i)
print(new_list)        