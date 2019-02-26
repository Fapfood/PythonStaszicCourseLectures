l1 = [i + 2 for i in range(5) if i % 2 == 0]
l2 = [[(i, j) for i in range(5)] for j in range(4)]
l3 = [(i, j) for i in range(5) for j in range(4)]
l4 = [(i, j) for i in range(4) if i % 2 == 1 for j in range(4) if i > j]
l5 = [(i, j) if i != j else 'ala' for i in range(4) if i % 2 == 1 for j in range(4) if i >= j]
s1 = {a for a in range(5)}
d1 = {a: str(a) for a in range(5)}