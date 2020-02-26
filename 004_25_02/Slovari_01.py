# Словари. Задание 1
# Предположим, что у всех сотрудников - разные фамилии. В таком случае - их фамилии
# можно использовать в качестве ключа
# Задаем словарь сотрудников
Empl = {
    "Иванов":['2', 'январь'],
    "Петров":['4', 'февраль'],
    "Смирнов" : ['30' , 'январь'] ,
    "Ворошилов" : ['28' , 'июнь'] ,
    "Уткин" : ['12' , 'июль'] ,
    "Карпин" : ['2' , 'февраль'] ,
    "Махно" : ['31' , 'декабрь'] ,
    "Кочубей" : ['16' , 'январь'] ,
    "Закариадзе" : ['18' , 'октябрь'] ,
    "Иванопуло" : ['1' , 'декабрь'] ,
    "Катышев" : ['25' , 'февраль'] ,
    "Лозовой" : ['8' , 'март'],
    "Асланов" : ['8' , 'январь'],
    "Кикабидзе" : ['8' , 'май'],
    "Абакумов" : ['28' , 'февраль'],
    "Цветков" : ['2' , 'февраль']
}
# Функция преобразования названия месяца
def MonthToMon(Mon):
    # Mon = Mon.lower()
    if Mon == "январь": Month = "января"
    if Mon == "февраль": Month = "февраля"
    if Mon == "март": Month = "марта"
    if Mon == "апрель": Month = "апреля"
    if Mon == "май": Month = "мая"
    if Mon == "июнь": Month = "июня"
    if Mon == "июль": Month = "июля"
    if Mon == "август": Month = "августа"
    if Mon == "сентябрь": Month = "сентября"
    if Mon == "октябрь": Month = "октября"
    if Mon == "ноябрь": Month = "ноября"
    if Mon == "декабрь": Month = "декабря"
    return Month

# Задаем словарь дней рождения в выбранном месяце
EmplBirthday = {}
BrdMonth = input("Введите месяц ")
print(BrdMonth)
for key, val in Empl.items():
    if val[1] == BrdMonth.lower():
        # Заполняем словарь выбранного месяца
        EmplBirthday.update({ key:val[0]+" " + MonthToMon(val[1]) })

# Вывод отсортированного списка ДР в выбранном месяце
list_key = list(EmplBirthday.keys())
list_key.sort()
for i in list_key:
    print (i, ":", EmplBirthday[i])

