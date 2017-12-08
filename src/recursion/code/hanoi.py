def hanoi(number, source, target, assistant):
    if number > 0:
        hanoi(number - 1, source, assistant, target)
        print('Moving {}th disk'.format(number),
              'from', source, 'to', target,
              'using', assistant, 'as assistant')
        hanoi(number - 1, assistant, target, source)


hanoi(4, 'A', 'B', 'C')
