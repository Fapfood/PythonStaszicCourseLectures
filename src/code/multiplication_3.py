def multiplication(i, j):
    def mul(i, j):
        if j == 1:
            return i
        return i + mul(i, j - 1)

    if i == 0 or j == 0:
        return 0
    if j < 0:
        return -multiplication(i, -j)
    if i < 0:
        return -multiplication(-i, j)
    if i < j:
        return multiplication(j, i)
    return mul(i, j)
