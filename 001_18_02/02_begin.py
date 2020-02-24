# Программа 01.02 - вычисление выражения
import math

x = 0.274
y = 34
# Вычисляем результат
s = (10 * x + 3 * math.sqrt(math.cos(x))) / (math.pow(y,2) - y * x)

print ("Результат = \t",s)
print ("Целая часть = \t", math.trunc(s))

