alist = [1, 2, 3]
print(id(alist))
atuple = (1, 2, 3)
print(id(atuple))
alist[0] = 10
print(id(alist))
# atuple[0] = 10
print(id(atuple))
atuple = (10, 2, 3)
print(id(atuple))