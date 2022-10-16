def srednia_wieku(**kwargs):
    suma = 0
    for name, age in kwargs.items():
        suma += age
    return suma / len(kwargs)


print(srednia_wieku(Janusz=5, Agata=3, Marta=10, Malgorzata=32))
print(srednia_wieku(Mateusz=15, Nikola=34, Bartlomiej=76, Malgorzata=32))
