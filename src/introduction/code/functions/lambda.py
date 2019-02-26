unnamed1 = lambda a, b: a + b
unnamed2 = lambda *nums: sum(nums)
unnamed3 = lambda a, b=6: a + b

print(unnamed1(1, 2))
print(unnamed2(1, 2, 3, 4))
print(unnamed3(1, 2))
print(unnamed3(1))

alist = [('ala', 3), ('ola', 5), ('ela', 2)]
alist.sort(key=lambda a: a[1])
print(alist)

def myfunc(n):
    return lambda a : a * n

print(myfunc(2)(3))