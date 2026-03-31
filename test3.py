from collections import defaultdict
import pandas as pd


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

sample = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9]

sr = pd.Series(sample)

print(sr.median())


my_dict = defaultdict(list)

for i in sample:
    # if i == 4:
    my_dict[i].append(i)


print(my_dict)

n = 2
for i in range(25):
    print('n=', i,  n**(i+1), n**(i+1)/2)

    # p += 2**i
    # if p > 140_000:
    #     break
    # print('p=', p, i, i**(2+1))


string = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested..."""

# with open("file.txt", "w") as f:
#     for line in string.split("\n"):
#         f.write(line.split()[0] + "\n")

# f = open("file1", "w")
# for line in string.split("\n"):
#     f.write(line.split()[0] + "\n")
# f.close()

with open("file.txt", "r") as f:
    for line in f:
        print(line.strip('\n'))
