# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

data1 = open('Exercise_5_1.txt', 'r')
file1 = data1.readline()

data2 = open('Exercise_5_2.txt', 'r')
file2 = data2.readline()

sum = file1 + file2

data = open('Exercise_5_3.txt', 'w')
data.writelines(sum)
data.close()
