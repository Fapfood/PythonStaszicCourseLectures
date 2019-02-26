alist = [1, '2', ['7/3', 2.5], 3.14, 4, 5, 6]
print(type(alist))
print(alist[0])
print(alist[2])
print(alist[-2])
print(alist * 2)
print(len(alist))
print('2' in alist)
print(2 in alist)
alist[4] = 100
print(alist)
alist[4] = 100
print(alist)
list2 = alist[2] + ['ala', 'ma', 'kota']
print(list2)