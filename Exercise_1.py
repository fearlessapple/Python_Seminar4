# Вычислить число c заданной точностью d

import math

num = math.pi
d = float(input("Input accuracy: "))
n = int(len(str(d))) - 2

print(f'pi = {round(num, n)}')