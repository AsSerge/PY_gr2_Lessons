# Программа 02.01 - подбор числа два способа
a = 343
b = 46
c = 235
# Первый способ
print("*" * 10, "Первый способ","*" * 10)
if a > b and a > c:
    print (a, "a - Максимальное число")
elif c > b and c > a:
    print (c, "c - Максимальное число")
elif b > c and b > a:
    print (b, "b - Максимальное число")

if a < b and a < c:
    print (a, "a - Минимальное число")
elif c < b and c < a:
    print (c, "c - Минимальное число")
elif b < c and b < a:
    print (b, "b - Минимальное число")

# Второй способ
print("*" * 10, "Второй способ","*" * 10)
l = []
l.append(a)
l.append(b)
l.append(c)
print ("Максимальное число",max(l))
print ("Минимальное число", min(l))