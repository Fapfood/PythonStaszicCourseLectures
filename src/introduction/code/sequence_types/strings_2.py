astring = 'konstantynopolitańczykiewiczówna'
print(astring.find('a'))
print(astring.index('a'))
print('poli' in astring)
print(astring.index('poli'))
print(astring.count('o'))
print(astring.count('cz'))
print(astring.split('o'))
print(astring.split('cz'))
print(astring.replace('cz', 'sz'))
print(astring.translate({ord('a'): ord('1')}))