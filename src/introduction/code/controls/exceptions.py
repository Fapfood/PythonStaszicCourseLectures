number = 0

try:
    if number < 0:
        raise RuntimeError('You can not use a negative number')
    else:
        print(1 / number)
except RuntimeError:
    print('Runtime exception')
except:
    print('Other exception')
finally:
    print('Always')