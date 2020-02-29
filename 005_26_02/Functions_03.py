# Задание 3
print("Сумма квадратов всех четных двузначных чисел:\t",sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10, 100)))))

# Сравнение
MyKey = print(">>>>>", sum(list(filter(lambda k: k % 4 == 0, range(10, 100)))))
Mk = []
for k in range(10, 100):
    if k % 4 == 0:
        Mk.append(k)
print (">>>>>", sum(Mk))











