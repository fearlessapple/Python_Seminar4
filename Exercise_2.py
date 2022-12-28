# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Input your number: '))

my_list = []

for i in range(2, n):
        

        my_list.append(i)


print(my_list)