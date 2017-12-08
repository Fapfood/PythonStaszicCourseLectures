def factorial(i):
    print('starting with', i)
    if i == 0:
        result = 1
    else:
        result = i * factorial(i - 1)
    print('ending with', i)
    return result


print(factorial(5))  # 120
