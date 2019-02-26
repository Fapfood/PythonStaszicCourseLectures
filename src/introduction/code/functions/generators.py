def square_generator(n):
    mylist = range(n)
    for i in mylist:
        yield i*i
        
for i in square_generator(5):
    print(i)