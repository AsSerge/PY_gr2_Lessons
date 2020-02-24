# Множетсва
one = {1,3,4,5,3,4,3,6,7,4,3,4,5,6,5,4}
two = {3,2,3,4,3,5,3,2,3,4,3,4,3,2,3,4}
# Получаем числа, входящие в оба множества, загоняем в список и сортируем его
union = sorted(list(one.intersection(two)))

raznost1 = list(one.difference(two))
raznost2 = list(two.difference(one))
print( "Это разные числа - их нет в каком-то из множеств", raznost1 + raznost2 )
print( "Это одинаковые - входящие в оба множества", union )
