def fibonacci(i):
    print('starting with', i)
    if i in [0, 1]:
        result = 1
    else:
        result = fibonacci(i - 1) + fibonacci(i - 2)
    print('ending with', i)
    return result


print(fibonacci(5))  # 8
