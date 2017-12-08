def multiplication(i, j):
    if j < 0:
        return -multiplication(i, -j)
    if j == 0:
        return 0
    if j == 1:
        return i
    return i + multiplication(i, j - 1)
