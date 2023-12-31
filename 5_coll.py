# *** Коллекции *** (контейнер, структуры данных итд)

# Списки (list)

# Список - это упорядоченная (проиндексированная), изменяемая (мутабельная) коллекция

# объекты внутри списка - элементы
#  каждый элемент проиндексирован

#  создание пустого списка
lst_1 = []
lst_1 = list()

# создание предварительно заполненных списков
lst_2 = [3, 5, 10, 55]
lst_3 = [20, 30, 3.14, "cool", "d", [1,2,3,4]]
lst_4 = list("cool")

# добавление элемента (объекта) в список 
# print(lst_1)

lst_1.append(100)

# print(lst_1)

lst_1.append("hi")

# print(lst_1)

lst_1.append("low")

lst_3.append("прива")

# чтение значений элементов
#  прямая инлексация (слева направо)
el_1 = lst_3[3]

lenght = len(lst_3)
last_el = lst_3[lenght -1]

# обратная индексация (справа на лево)
last_el = lst_3[-1]

# замена значений
lst_3[1] = "куку"
lst_3[2] = "ПИ"

# print(lst_3)
# удаление элемента
# по индексу
# del lst_3[0]

# print(lst_3)

# del lst_3[2]

# по значению
# lst_3.remove("прива")

# очистка списка
# lst_3.clear()

# срезы списка
lst_5 = list('Hello, World!')

# срез от начала до конца
# slice_1 = lst_5[4:11]
slice_1 = lst_5[:]   # от начала до конца

# срез от начала до индекса В (не включительно)

slice_1 = lst_5[:5]

# срез от индекса А до конца списка
slice_1 = lst_5[5:]

# срез от индекса А до индекса Б (не включительно)
slice_1 = lst_5[0:2]

# срез от начала до конца с шагом 2
slice_1 = lst_5[0:10:2]

# срез по отрицательным индексами с отрицательным шагом

print(slice_1)

