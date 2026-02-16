import pickle
import json
import sys

obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}

with open('file.pkl', 'wb') as file:
    pickle.dump(obj, file)

with open('file.pkl', 'rb') as file:     # используется файл, полученный на предыдущем шаге
    obj = pickle.load(file)
    print(obj)
    print(type(obj))


binary_obj = pickle.dumps(obj)

print(binary_obj)
print(type(binary_obj))


obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
binary_obj = pickle.dumps(obj)

new_obj = pickle.loads(binary_obj)

print(id(new_obj), id(obj), new_obj == obj)

a = [7, 8]
b = [7, 8]
print(a == b, id(a), id(b), id([7, 8]))
print(a is b)
print(new_obj)


# def func(*args):
#     return '-'.join(args)


# with open("diary.txt", encoding="UTF-8") as inputf:
#     sys.stdin = inputf
#     data = sys.stdin.readlines()

# sys.stdin = sys.__stdin__

# print(data[0].strip('\n'), *map(lambda i: i.strip('\n'), data[1:]))

# with open(data[0].strip('\n'), 'rb') as file:
#     # print(file.read())

#     obj = pickle.load(file)
# print(obj(*map(lambda i: i.strip('\n'), data[1:])))

# def func(*args):
#     return '-'.join(args)

# with open("func.pkl", "wb") as f:
#     pickle.dump(func, f)

# with open('func.pkl', 'rb') as file:     # используется файл, полученный на предыдущем шаге
#     obj = pickle.load(file)
#     print(obj(*['1', '2']))
#     print(type(obj))


# def filter_dump(filename, objects, typename):
#     # res = list(filter(lambda x: type(x) is typename, objects))
#     res = [obj for obj in objects if type(obj) is typename]
#     with open(filename, "wb") as f:
#         pickle.dump(res, f)


# filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)

# with open('numbers.pkl', 'rb') as file:     # используется файл, полученный на предыдущем шаге
#     obj = pickle.load(file)
#     print(obj)
#     print(type(obj))


# with open("diary.txt", encoding="UTF-8") as inputf:
#     sys.stdin = inputf
#     # data = sys.stdin.readlines()  						 #['func.pkl\n', 'g\n', 'f\n', 'j']
#     # data1 = [s.rstrip('\n') for s in sys.stdin.readlines()] #['func.pkl', 'g', 'f', 'j']
#     data3 = [line for line in sys.stdin]


# sys.stdin = sys.__stdin__

# print(data3)
print()

obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
obj = ['a', 'b', 3, 4, 'f', 'g', 7, 8], 24

with open('file.pkl', 'wb') as file:
    pickle.dump(obj, file)

with open('file.pkl', 'rb') as file:     # используется файл, полученный на предыдущем шаге
    obj = pickle.load(file)
    print(obj[1], obj[0])
    cs = obj[1]
    obj_out = obj[0]
    res = [i for i in obj_out if type(i) is int]
    if type(obj_out) is list:
        res = [i for i in obj_out if type(i) is int]
        cs_out = min(res)*max(res)
    else:
        cs_out = sum(res)
    print(f'Контрольные суммы {'' if cs == cs_out else 'yt'}совпадают')
