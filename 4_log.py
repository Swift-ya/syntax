# операция сравнения

x = -3
y = 3

# операция меньше
# мы спрашиваем значения х меньше значения у?
res = x < y 

# операция меньше либо равно
# мы спрашиваем значения х меньше или равно у?
res = x <= y 

# операция больше
# мы спрашиваем значения х больше ?
res = x > y 

# операция больше либо равно
# мы спрашиваем значения х больше или равно?
res = x >= y 

# операция равенства
# мы спрашиваем значения х равно у?
res = x == y 

# операция неравенства
# мы спрашиваем значения х неравен у?
res = x != y 

# print(res)


# логические операции

v_1 = True
v_2 = False

# оператор "НЕ" (NOT, иверция, отрицание)
res = not v_1

# оператор "И" (AND, конъюнкция, логическое умножение)
# возвращает True только тогда, когда оба значения True
res = v_1 and v_2

# оператор "ИЛИ" (OR, дизъюнкция, логическое сложение)
# возвращает False только тогда, когда оба значения False
res = v_1 or v_2 

# print(res)

a = 3 
b = 0

res = (a < 5) and (b == 0)

# print(res)


# условные операции 

a = 5 

# оператор if (если)
# if a == 0:
#     print("hello!")

# оператор esle (иначе)
b = 2

# if b < 20:
#     res = "меньше 20"
# else:
#     res = "больше либо равно 20"

# оператор elif (else if)
a = 0

res = ""

if a > 0:
    res = "больше нуля"
elif a < 0:
    res = "меньше нуля"
else:
    res = "=0"

# print(res)


# пример простого калькулятора

value_1 = int(input("введите 1 число: "))
value_2 = int(input("введите 2 число: "))

operator = input("введите операцию: ")

if operator == '+':
    result = value_1 + value_2
elif operator == '-':
    result = value_1 - value_2
elif operator == '*':
    result = value_1 * value_2
elif operator == '/':
    result = value_1 / value_2
else:
    result = "Введи нормально РРРррррр"

print(f"Вот оно МЗФК = {result}")