def null_dec(func):
    y = 123
    return func(y)


def greet(y):
    print('123!')
    return '222!' + str(y)


greet1 = null_dec(greet)

print(greet1)

d = {'sep1': '\n'}
print('123-', '-321', **{'sep': '\n', 'end': '!'})

print()
l = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
sr = sum(l)/len(l)
l1 = sum([(i-sr)**2 for i in l])/(len(l)-1)
print(l1**(0.5))
