num_1 = int(input("1 игрок введите число: "))

num_2 = int(input("2 игрок угадай число: "))

if num_1 < num_2:
    print("меньше!!!")
    num_2 = int(input("2 игрок угадай число: "))
elif num_1 > num_2:
    print("больше!!!")
    num_2 = int(input("2 игрок угадай число: "))


else:
    print("МОЛОДЕЦ!!!")




