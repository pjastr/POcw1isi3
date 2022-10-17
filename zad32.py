import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]
randomlist2 = randomlist.copy()
randomlist2.sort()

print(randomlist2[:3])
print(randomlist2[-3:])
