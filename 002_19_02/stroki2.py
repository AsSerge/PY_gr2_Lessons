# Слова для перебора
CheckMyWords = ["шалаш", "сабля", "шиш", "самолет","азиза","кучук","весло","потоп","топот","грамота"]
# Функция проверки на Палиндром
def CheckWord(MyWord):
    if MyWord[::-1] == MyWord:
        print("Слово", MyWord, "- Палиндром!")
    else:
        print ( "Слово" , MyWord , "- простое слово" )
# Проверка
for Mword in CheckMyWords:
    CheckWord(Mword)
