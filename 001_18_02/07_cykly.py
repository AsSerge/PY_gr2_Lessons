# Программа 03.02 - Сумма факториалов
import math
num_1 = 1
summ_all = 0
while num_1 <= 12:
    f = math.factorial(num_1)
    print(num_1, "\t", f)
    summ_all = summ_all + f 
    num_1 += 1
print ("******************")
print ("Сумма:\t",summ_all)