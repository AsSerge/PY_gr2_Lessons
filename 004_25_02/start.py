str = [float(i**2) for i in range(1, 101)]
for i in str:
    print(i)
lst = list(str)
tpl = tuple(str)
print(lst.__sizeof__())
print(tpl.__sizeof__())
