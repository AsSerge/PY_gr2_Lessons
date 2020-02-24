# Найти среднее арифметическое и медиану в последовательности чисел.
# Ввод данных, разделенных пробелом
Start_String = "12.34 14.45 14.75 45.21 16.23 78.21 56.48 14.36 15.85 95.15 14.0 23.12"
# Преобразование данных в список
text_Data = Start_String.split(" ")
# Преобразование формата данных в списке
float_data = [float(item) for item in text_Data] 
# Сортировка списка по возрастанию
float_data.sort()
#print(float_data)
print("Упорядоченный ряд")
print(float_data)

if len(float_data) % 2:
    # Если количество чисел в ряде НЕЧЕТНОЕ - берем среднее число
    mediana = float_data[int(len(float_data)/2)]
else:
    # Если количество чисел в ряде ЧЕТНОЕ - берем полусумму двух чисел в центре
    med = int(len(float_data)/2)
    m1 = float_data[med-1]
    m2 = float_data[med]
    mediana = (m1 + m2)/2
print ("Сренднее арифметическое:", round(sum(float_data)/len(float_data),2))
print ("Медиана:", mediana)


