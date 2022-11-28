import random
import statistics

random.seed(162681)
randomList = [random.randrange(1, 101) for i in range(200)]


def median(tab):
    sortlist = tab.copy()
    sortlist.sort()
    lng = len(sortlist)
    if lng % 2 == 0:
        median = (sortlist[(lng - 1) // 2] + sortlist[lng // 2]) / 2
    else:
        median = sortlist[lng // 2]

    return median


print(f'Wbudowana mediana: {statistics.median(randomList)}')
print(f'Moja mediana: {median(randomList)}')
