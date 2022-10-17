def silnia_p(n: int) -> int:
    s = 1
    for x in range(1,n+1):
        s *= x
    return s

print(silnia_p(5))