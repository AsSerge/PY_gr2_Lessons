MyString = "??первый      второй третий    ?? четвертый пятый шестой    ?? седьмой       восьмой девятый    десятый"
# Делим строку по пробельному символу и пишем в Список
StringToWork = MyString.split(" ")
# Создаем список для новой строки
NewString = []
for k in StringToWork:
    if k != "" and k != "??":
        NewString.append(k.replace('??', ''))
print("Исходная строка")
print (MyString)
print ("Найдено:",len(NewString),"слов")
print(" ".join(NewString))