import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]


def minimum(lista):
    temp = lista[0]
    for x in lista:
        if temp > x:
            temp = x
    return temp


print(minimum(randomlist))
liczba = min(randomlist)
print(liczba)
