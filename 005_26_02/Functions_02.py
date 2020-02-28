# Задание 2
# Инфофункция
def statistics(arr):
    print("Список: ", end="")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("")
    print ( "Число элементов:\t" , len(arr) )
    print ( "Среднее знечение:\t" , round(sum(arr)/len(arr), 2))
    print ( "Максимальный эелмент:\t" , max(arr))
    print ( "Минимальный элемент:\t" ,  min(arr))


# Задаем список целых чисел
MyList = [10, 33, 18, 3, 2, 43, 41, 41, 9, 47, 42, 29, 27, 42, 13, 15, 16, 23, 21]
# Вызываем "Инфофункцию"
statistics(MyList)