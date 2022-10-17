import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]
Sum = 0
for i in randomlist:
    if i > 99:
        Sum += 1
print(Sum)
