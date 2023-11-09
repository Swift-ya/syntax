# калькулятор

print("Добро пожаловать в простой КАЛЬКУЛЯТОР")

value_1 = int(input("введите 1 число: "))

operator = input("введите операцию: ")

value_2 = int(input("введите 2 число: "))



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

print(f"Держи ответ: = {result}")