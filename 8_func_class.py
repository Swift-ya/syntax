# *** функция ***

# создание функции
# не обладает параметрами и ничего не возвращает
def func_1():
    print("hello from func_1")

# обладает параметрами и ничего не возвращает
def func_2(par_0, par_2, par_1=5):
    res = par_0 + par_1
    print(res)

# обладает параметрами и возвращает что-то
def func_3(par_1):
    res = par_1 ** 2
    return res 
    
# вызов функции
# func_2(10, 30, 40)
# result = func_3(10)
# print(result)


# *** классы ***

class Cat:
    # метод конструктор
    def __init__(self, name, a):
        # атрибуты
        self.name = name
        self.age = a
    
    # метод экземпляра - функция объекта
    def myau(self):
        res = f"мяу-мяу! меня зовут {self.name}!!! и мне {self.age} года"
        print(res)

# создание экземпляров (объектов) класса Cat
c_0 = Cat("Boss", 2)
c_1 = Cat("Murya", 1)
c_2 = Cat("Suchka", 4)

# вызов метода
c_0.myau()
c_1.myau()

# работа с атрибутами
# c_2.name = "мурек"

# print(c_2.name)

c_2.myau()

# функции более подробно
# объектно-ориентированное программирование