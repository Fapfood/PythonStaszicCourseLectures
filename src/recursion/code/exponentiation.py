def exponentiation(i, j):
    if j == 1:
        return i
    if j == 0:
        if i == 0:
            return 'ERR'
        return 1
    if j > 0:
        return i * exponentiation(i, j - 1)
    return exponentiation(1 / i, -j)
