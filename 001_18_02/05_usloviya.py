# Программа 02.03 - Загадки
answer = 0
answer_error = []
print("1. Тело деревянное, одежда рваная, не ест, не пьет, огород стережет.")
print("\tA. Пиноккио.")
print("\tБ. Огородник.")
print("\tB. Пугало.")
answer1 = input("Введите букву А, Б или В, соответствующую правильному ответу ")
if answer1 == "В":
    answer += 1
else:
    answer_error.append("1")
print("2. В морях и реках обитает, но часто по небу летает, а как наскучит ей летать, на землю падает опять.")
print("\tА. Пеликан.")
print("\tБ. Вода.")
print("\tВ. Самолет-амфибия.")
answer2 = input("Введите букву А, Б или В, соответствующую правильному ответу ")
if answer2 == "Б":
    answer += 1
else:
    answer_error.append("2")
print("3. Пришла без красок и без кисти и перекрасила все листья.")
print("\tA. Девочка, занимающаяся граффити.")
print("\tБ. Осень.")
print("\tB. Коза.")
answer3 = input("Введите букву А, Б или В, соответствующую правильному ответу ")
if answer3 == "Б":
    answer += 1
else:
    answer_error.append("3")
print("4. Он пыхтит, как паровоз, важно кверху держит нос, пошумит, остепенится, пригласит чайку напиться.")
print("\tA. Шеф.")
print("\tБ. Сосед-пенсионер.")
print("\tB. Чайник.")
answer4 = input("Введите бкву А, Б или В, соответствующую правильному ответу ")
if answer4 == "В":
    answer += 1
else:
    answer_error.append("4")
print("5. Под водой живет народ, ходит задом наперед.")
print("\tA. Дайверы.")
print("\tБ. Водяной и его слуги.")
print("\tB. Раки.")
answer5 = input("Введите букву А, Б или В, соответствующую правильному ответу ")
if answer5 == "В":
    answer += 1
else:
    answer_error.append("5")    
print("*"*35)   
print("Количество правильных ответов:", answer)
if answer == 5:
    print("Поздравляем! Вы правильно ответили на все вопросы!")
else:
    print("Вам нужно подумать над вопросами: ", " ".join(answer_error))


