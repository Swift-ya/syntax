# программа с графическим пользовательским интерфейсом (GUI)

# *** Генератор паролей ***

# импортирование модулей
import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar

# основная функция 
def pwdGenerator(pwd_str: str) -> str:
    # кодирование в байт строку
    byte_str = pwd_str.encode()
    # хеширование
    hash_str = hashlib.sha256(byte_str)
    # преобразование в обычную строку
    hex_str = hash_str.hexdigest()[:10]
    # возврат хеш строки
    return hex_str

# тестирование функции
# while True:
#     pwd = input("Введите пароль: ")
#     if pwd == "stop":
#         break
#     res = pwdGenerator(pwd)
#     print(res)

# объект окна
app = Tk()

# объекты для хранения строк
raw_pwd = StringVar()
result = StringVar()

# виджет текстовой метки
Label(text="Пароль:").grid(row=0, column=0)

# виджет поля ввода пароля
Entry(textvariable=raw_pwd).grid(row=0, column=1)

# виджет кнопки
def btn_func():
    result.set(pwdGenerator(raw_pwd.get()))
Button(text="START", command=btn_func).grid(row=1, column=0)

# виджет поля вывода результата
Entry(textvariable=result).grid(row=1, column=1)

# точка входапрограммы
app.mainloop()