# Импортируем модуль для работы с CSV - вместо пробела - используем ";"
import csv
# Читаем файл и помещаем его в список
with open('product_list.csv', 'r', encoding = 'UTF-8') as fp:
    reader = csv.reader(fp, delimiter=';', quotechar='"')
    data_read = [row for row in reader]

for i in data_read: print (i)

# Создаем новое множество покупателей (значения  - уникальны)
Buyers = set()
for k in data_read:
    t = k[0]
    Buyers.update( t )
print(Buyers)





