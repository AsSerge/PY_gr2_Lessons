# Задание 1
# Функция для вычисления среднего арифметического ряда случайных сисел
import random as rnd
# Функция вычисления среднего арифметического ряда чисел
def average_fn(Row):
    # Возвращает среднее округленное до двух знаков
    return round(sum(Row)/len(Row), 2)


# Получаем случайное количество чисел ряда
MyCount = rnd.randrange(10, 20, 1)
print ("Количество чисел ряда:\t", MyCount, "(случайное число)")
# Получаем ряд случайных чисел
MyRow = list()
for k in range(MyCount):
    MyRow.append(rnd.randrange(1, 50, 1))
print("Случайные числа (1-50):\t", MyRow)
print("Среднее арифметическое:\t",average_fn(MyRow))



