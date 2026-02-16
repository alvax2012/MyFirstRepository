

num2 = [102, 1]
print(id(num2))
num = num2  # [102, 1]
num2.append(3)  # = [102, 1, 7]
print(id(num), id(num2))
print(num, num2)

# num2 = 4
# print(id(num2))
# print(id(num))

num22 = 1  # [102, 1]
print(id(num22))
num11 = num22  # [102, 1]
num22 = 11  # [102, 1]
print(id(num11), id(num22))

print('1=', id(list))


data = ['b', 'e', 'e', 'g', 'e', 'e', 'k']
print(id(data))
data[0] = 'B'
print(id(data))

print(data)
