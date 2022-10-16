# zad 25
import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]
randomlist.sort()

for i in range(20):
    print(i + 1, ". ", randomlist[i])

print(randomlist[:20])
