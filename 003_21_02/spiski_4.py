Line = int(input(">>>Введите количество строк для нововой таблицы "))
Column = 3 # Прибито
table = [input(">>>Введите элементы строки, разделенные запятой: ").split(',') for i in range(Line)]

print("*****************Таблица*****************")
for i in range(Line):
    for j in range(Column):
        print(table[i][j], "("+str(i)+","+str(j)+")",end="\t")
    print("")    
print("*****************************************")

Item = int(input(">>>Введите количество выводимых эелементов: "))
Coord = [input(">>>Введите координаты, разделенные запятой: ").split(',') for i in range(Item)]

print("**********************************************")
print ("Найдены элементы:")
for i in range(Item):
    x = int(Coord[i][0])
    y = int(Coord[i][1])
    print(str(x)+","+str(y),table[x][y], sep = " - ")
print("**********************************************")
print("Конец цикла исследований")

    
        
        
    

