i = 0
while i < 5:
    print(i)
    i += 1

stack = ['ala', 'ola', 'ela']
while len(stack) > 0:
    print(stack.pop())
else:
    print('now empty; length: ' + str(len(stack)))