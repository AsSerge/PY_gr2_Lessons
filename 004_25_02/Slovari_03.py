# Импортируем модуль для работы с CSV - вместо пробела - используем ";"
import csv
# Читаем файл и помещаем его в список
with open('product_list.csv', 'r', encoding = 'UTF-8') as fp:
    reader = csv.reader(fp, delimiter=';', quotechar='"')
    data_read = [row for row in reader]

# Создаем новое множество покупателей (значения  - уникальны)
Buyer = set()
for i in data_read: Buyer.add(i[0])
Buyer = sorted(list(Buyer)) # сортируем список покупателей по алфавиту

# Выводим список покупателей и купленны х ими продукутов
print("*"*40)
for BuyerMame in Buyer:
    print("\tПокупатель:",BuyerMame)
    GoodsArr = {} # Создаем список продуктов
    for Purchase in data_read:
        if Purchase[0] == BuyerMame:
            Goods = Purchase[1]
            GoodsNumber = int(Purchase[2])
            # Заполняем список
            if not Goods in GoodsArr:
                GoodsArr.update( {Goods:GoodsNumber} )
            else:
                GoodsNumber = int(GoodsArr[Goods]) + int(Purchase[2])
                GoodsArr.update ( {Goods : GoodsNumber} )

    # Здесь выводим отсортированный по ключу список товаров для каждого покупателя
    list_key = list ( GoodsArr.keys () )
    list_key.sort ()
    for i in list_key :
        print ( "\t", i , ":" , GoodsArr[i] )
    print("*"*40)


