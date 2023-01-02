# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Input your number: '))

my_list = []

i = 2

while i <= n:
    if n % i == 0:
        n = n // i
        my_list.append(i)
        i = 2
    else:
        i = i + 1
print(my_list)
