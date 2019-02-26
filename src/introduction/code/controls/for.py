for i, s in [(1, 'a'), (2, 'b'), (3, 'c')]:
    print(s * i)
    print('---' * i)

for i in range(3, 8):
    print(i)
else:
    print('end')

for i in 'aleksandra':
    print(i)

for i, val in enumerate('aleksandra'):
    print(i * val)