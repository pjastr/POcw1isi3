def silnia_rek(n: int) -> int:
    if n == 1:
        return 1
    return n * silnia_rek(n - 1)


print(silnia_rek(10))
