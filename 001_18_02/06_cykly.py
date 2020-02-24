# Программа 03.01 - Вещественные и целые числа
import math
n = 23.2343
m = 14.2345
# Определяем бОльшее число
if m > n:
    k1 = n
    k2 = m
else:
    k1 = m
    k2 = n

counter = 1
for k in range(math.trunc(k1) + 1, math.trunc(k2) + 1):
    print (k)
    counter = counter * k
print (counter)