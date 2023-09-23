from random import*
for i in range(randint(-1000, 1000)):
    if i > 0:
        i = bin(i)[2:]
    else:
        i = 'Неверный ввод'
print(i)