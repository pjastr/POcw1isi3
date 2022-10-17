import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]

lel = []
for x in randomlist:
    if randomlist.count(x) == 3:
        if x not in lel:
            lel.append(x)
            
print(lel)
