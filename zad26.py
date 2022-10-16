# zad 26
import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]
iloczyn = 1

for i in randomlist:
    iloczyn = i * iloczyn

print("Iloczyn: ", iloczyn)
