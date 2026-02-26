from collections import namedtuple


Person1 = namedtuple('Person2', ['name', 'children'])

sveta = Person1('Sveta Gueva', ['Larisa', 'Timur'])
print(sveta)

sveta.children.append('Soslan')
print(sveta)
