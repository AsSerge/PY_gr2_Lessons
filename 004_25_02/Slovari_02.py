# Создаем и заполняем список дат месяца
Month = ['{:02}'.format(i) for i in range(1,32)]
MonthName = "Дубабрь 2020"
# Задаем график работы для всех сотрудников [1 - каждый день, 2 - сутки сеиез сутки, 3 - сутки / двое]
Schedule = 3
# Формируем словарь
Empl = {
    "Иванов":[k for k in Month[::Schedule]],
    "Петров":[k for k in Month[1::Schedule]],
    "Смирнов":[k for k in Month[2::Schedule]],
    "Ворошилов":[k for k in Month[::Schedule]],
    "Карпин" : [k for k in Month[1: :Schedule]]
}
# Выводим общий гафик по компании
print("Месяц: "+MonthName)
for key, value in Empl.items():
    print(key, ":\t", " | ".join(value))
# Выводим график по отдельному сотруднику
print("Введите 'End' для выхода")
OneEmpl = ""
while OneEmpl != "End":
    OneEmpl = input("Введите фамилию сотрудника ")
    if OneEmpl == 'End':
        break
    if OneEmpl in Empl:
        print(OneEmpl, ":\t", " | ".join(Empl[OneEmpl]))
    else:
        print("Нет такого сотрудника")

