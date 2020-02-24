print ("Для окончание игры введите слово \"Stop\"")

# Функция сравнения последней буквы первого сгорода с первой буквой второго
def CheckWordsLetter(FirstCity, SecondCity):
    FirstCity_LastLetter = FirstCity[-1].lower ()  # приводим к нижнему регистру
    if FirstCity_LastLetter == "ь":
        FirstCity_LastLetter = FirstCity[-2].lower ()  # приводим к нижнему регистру
    SecondCity_FirstLetter = SecondCity[0].lower ()  # приводим к нижнему регистру
    if FirstCity_LastLetter == SecondCity_FirstLetter:
        return True

FirstCity = input ( "НАЧАЛО: Введите название города: " )
while FirstCity != "Stop":
    SecondCity = input ( "Введите название следующего города: " )
    if SecondCity == "Stop":
        break
    while not CheckWordsLetter(FirstCity, SecondCity):
        print("НЕВЕРНО")
        print("Вам на", FirstCity[-1].upper ())
        SecondCity = input ( "Введите правильное название города: " )
        if SecondCity == "Stop" :
            break
    print ( "ВЕРНО", FirstCity, " - ", SecondCity)
    FirstCity = SecondCity


