# ***циклы***

# оператор while

# бессконечный цикл
# while True:
#     print("hello")

# цикл с условием
# val = 0

# while val <= 10:
#     print(f"значение: {val}")
#     # инкремент - увеличение значений
#     # длинный вариант
#     # val = val + 1
#     # короткий вариант
#     val += 1

# while val > -10:
#     print(val)
#     # декримент - уменшение значений 
#     val -= 1

# прерывание по дополнительному условию

# while True:
#     val = input("enter the name: ")
#     if val == "stop":
#         print("bye-bye!!!")
#         break
#     print(f"hello, {val}!")

val = 10

# while val > 0:
#     print(val)
#     val -= 1
#     if val < 5:
#         break

# пропуск части кода тела цикла

# val = 0 

# while val <  20:
#     #  1 кусок кода
#     print(val)
#     val += 1 

#     # if val > 10:
#     #     continue

#     # # 2 кусок кода 
#     # print("hello")

#     if val < 10:
#         continue

#     # 2 кусок кода 
#     break

# оператор for

# 1. "чтение" значения итерируемого объекта по порядку
# 2. каждое считанное значение присваевается в собственную переменную
# 3. выполняет блок кода своего тела

list_0 = [10, 20, 4, 2, 1000, 478]

# for var in list_0:
#     var *= 10
#     print(var)

my_dict = dict(a=100, b=200, c=300)

# print(my_dict)

# for item in my_dict.items():
#     print(item)

# for key, val in my_dict.items():
#     print(f"ключ: {key}, значение: {val}")

# for char in "hello, world!":
#     print(char)

# класс range()

r = range(0, 10)
r = range(0, 20, 2)

# print(tuple(r))

# for num in range(10):
#     print(num)

# безимянная переменная
for _ in range(5):
    print("hello")

    # генератор списка 
    # генератор словаря