viruchka = int(input('Введите выручку:')) # строка
ubitok = int(input('Введите издержки:')) # строка

if viruchka > ubitok:
    print("Вы работаете в плюс")
    print("Рентабельность ", (viruchka - ubitok) / viruchka )
    count = int(input('Сколько у вас сотрудников:'))  # строка
    p = (viruchka - ubitok) / count
    print("Средняя прибыль на одного сторудника: ", p)

elif viruchka < ubitok:
    print("Вы работаете в минус")
elif viruchka == ubitok:
    print("Вы работаете в ноль")


