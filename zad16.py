def foo(*arg):
    suma = 0
    for x in arg:
        suma += x ** 2

    return suma


print(foo(3, 4, 5))
print(foo(1, 2, -1, 2))
