stack = ['ala', 'ola', 'ela']
while True:
    if len(stack) == 0:
        break
    print(stack.pop())

for i in range(6):
    if i in [1, 2, 4]:
        continue
    print(i)