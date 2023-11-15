# ***коллекции***

# кортеж (tuple)

# упорядоченная неизменяемая (иммутабельная) коллекция

# создание предварительно заполненного кортежа
tuple_1 = (10, 20, 30, 0, 5, 3)                  
tuple_1 = tuple([1, 200, 3.14, "hello"])
tuple_1 = tuple("hello, tuple")

# чтение значений
val_1 = tuple_1[-1]

# срез кортежа
slice_1 = tuple_1[1:3]
slice_1 = tuple_1[::-2]


# print(slice_1)

# словарь (dict, dictionary)

# неупорядоченная изменяемая коллекция

# элемент словаря пара "ключ значения"

# создание пустого словаря
dict_1 = {}
dict_1 = dict()

# создание предварительно заполненного словаря
dict_2 = {7:1000, 0:3.14, "A":20, 'abs':"python", "кортеж":(1,2,3)}

lst_1 = [(10, 20),("k", "v"),(3, dict_2)]
dict_3 = dict(lst_1)

dict_3 = dict(a=200, b=300)

# чтение значения
val_1 = dict_2[0]
# print(val_1)
val_1 = dict_2["A"]
# print(val_1)
    
# добавление пары
dict_2['B'] = 888
dict_2['C'] = "stroka"

# замена значения 
dict_2[0] = 'Пи'

# удаление пары 
del dict_2['abs']

# методы
print(dict_2)

# items_0 = dict_2.items()
items_0 = list(dict_2.items())
values_0 = list(dict_2.values())
keys_0 = list(dict_2.keys())

val_2 = dict_2.pop('A')

print(val_2)
print(dict_2)

# методы кортежа?
# остальные методы словаря?
# множество (set) тоже неупорядоченная коллекция? 