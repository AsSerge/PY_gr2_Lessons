# Создаем и заполняем список дат месяца
Month = [i for i in range(1,32)]
Empl = {
    "Иванов":[k for k in Month[::3]],
    "Петров":[k for k in Month[1::3]],
    "Смирнов" :[k for k in Month[2::3]]
}
print(Empl)
# print(Month)