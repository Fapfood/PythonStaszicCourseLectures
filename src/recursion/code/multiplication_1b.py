E, C, O = 0, 0, 0


def multiplication(i, j):
    global E
    global C
    global O
    C += 1
    E += 1
    if j < 0:
        O += 3
        return -i + multiplication(i, j + 1)
    E += 1
    if j == 0:
        return 0
    E += 1
    if j == 1:
        return i
    O += 2
    return i + multiplication(i, j - 1)


print(multiplication(-2, -5), E, C, O)
