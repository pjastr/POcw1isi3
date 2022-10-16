# zad 24
import random
import statistics

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]
sortlist = randomlist.copy()
sortlist.sort()

n = len(sortlist)
if n % 2 == 0:
    med = (sortlist[n // 2] + sortlist[n // 2 + 1]) / 2
else:
    med = sortlist[((n + 1) // 2)]

print(med)
print(statistics.median(randomlist))
