import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]

print(randomlist)


def suma_listy(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma


print(suma_listy(randomlist))
##drugi sposob
print(sum(randomlist))
