from collections import namedtuple


Person1 = namedtuple('Person2', ['name', 'children'])

sveta = Person1('Sveta Gueva', ['Larisa', 'Timur'])
print(sveta)

sveta.children.append('Soslan')
print(sveta)


p = namedtuple('Person', {'name': 1, 'male': 2, 'age': 3}, defaults=[None]*2)

ss = p(11)
print(ss.name)
