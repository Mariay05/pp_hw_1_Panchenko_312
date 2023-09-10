from random import randint
for n in range(-1000, 1000):
    n2 = bin(n)[:2]
    if n < 0:
        print("Неверный ввод")
    else:
        print(n2)