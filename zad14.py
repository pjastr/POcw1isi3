def palindrom(a: str) -> bool:
    for x in range(len(a) // 2):
        if a[x] != a[len(a) - 1 - x]:
            return False
    return True


print(palindrom("AMOGUS"))
print(palindrom("SUGOMAAMOGUS"))
