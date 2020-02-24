ListNumber = [12,34,65,34,76,23,89,54,23,65,89,10,23,1,32,4,5,7,8,12,34]
LString = [str(i) for i in ListNumber]
LString = " ".join(LString) 
print ("Исходный список:", LString)
print ("Наибольшее значение в списке =", max(ListNumber))
print ("Индекс первого вхождения наибольшего значения:", ListNumber.index(max(ListNumber)))
