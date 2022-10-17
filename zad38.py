def sortuj(x):
    a = []
    b = []
    for y in x:
        if y % 2 == 0:
            a.append(y)
        else:
            b.append(y)
    a.sort()
    b.sort(reverse=True)
    return a + b


l = [2, -3, 4, 9, 2]
l = sortuj(l)
print(l)
