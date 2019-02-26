def foo1(first, second, *rest, **named_rest):
    print('First: {}'.format(first))
    print('Second: {}'.format(second))
    print('And all the rest... {}'.format(list(rest)))
    print('And all the rest again... {}'.format(dict(named_rest)))

def foo2(string, multiplier=3):
    return first * multiplier

def foo3(elem, acc=list()):
    acc.append(elem)
    return acc

foo1(1, 2, 3, 4, 5, six=6, seven=7)