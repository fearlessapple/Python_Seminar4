# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Input your number: '))

c = []

for i in range(k+1):
    c.append(randint(0, 100))

p = str(c[0])

for j in range(1, k+1):
    p = str(c[j]) + '*x^' + str(j) + ' ' + '+' + ' ' + p

print(p)

data = open('Exercise_4.txt', 'w')
data.writelines(p)
data.close()
