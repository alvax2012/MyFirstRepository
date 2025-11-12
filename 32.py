c = '905 678123 45612 56'
def t(c): return '*' * 12 + c.replace(' ', '')[-4:]


print(t(c))
