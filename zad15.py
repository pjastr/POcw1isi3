z15_l1 = [1, 4, 6, 8, 12, 543, 876, 890, 1000]
z15_l2 = z15_l1[::-1]


def sortowan_rosnaco(l: list):
    p = None
    for x in l:
        if p is None or x < p:
            p = x
        else:
            return False
    return True


print(sortowan_rosnaco(z15_l1))
print(sortowan_rosnaco(z15_l2))
