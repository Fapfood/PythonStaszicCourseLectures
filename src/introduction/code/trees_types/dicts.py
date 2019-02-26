adict = {'a': 1, 'b': 2}
print(adict)
print(adict['a'])
print(adict.get('a'))
print(adict.get('c'))
print(adict.get('c', 'empty'))
print(len(adict))
print(adict.keys())
print(list(adict.keys()))
print(adict.values())
print(adict.items())
print(list(adict.items()))
print('c' in adict)
for k in adict:
    print(adict[k])
del adict['a']
print(adict)