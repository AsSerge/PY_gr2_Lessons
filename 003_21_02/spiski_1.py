# Задание 1.
# Написать программу сортировки списка по алгоритму «Сортировка выбором».
# Задаем несортированный список уникальных натуральных чисел
#StartList = [-2,5,6,3,8,13,10,19,-3,11,15,17,-5,20,16,9,7,-4,14,4,12,1,2,0,-1]

StartList = [22,45,32,56,54,3,56,34,78,65,-23,0,-45,23,655,4,3,2,1,1]
print("Исходный список\t",StartList)
# Предположим, что мы знаем функцию Python sort() и не можем написать StartList.sort():
# StartList.sort()
# Предположим, что мы не знаем некотороые функции Python, например sort() и min() 
# Функция для нахождения минимального элемента в списке
def GetMinItem(StartList):
    MinItem = StartList[0]  # предположим - минимальный элемент первый и равен StartList[0]
    for i in range(1, len(StartList)):
        if StartList[i] < MinItem:
            MinItem = StartList[i] # если очередной элемент меньше, то он и есть минимальный    
    return MinItem
# Создаем новый список для временного хранение результатов
NewList = []

for i in range(len(StartList)):
    M = GetMinItem(StartList) # Ищем минимальное значение
    NewList.append(M) # Добавляем его во временный список
    del StartList[StartList.index(M)] # Удаляем это значение из основного списка

print("*********************************************************************************************")
StartList = NewList # Обновляем основной список
print("Результат\t",StartList)




