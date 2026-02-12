import pickle
import json

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


# with open("diary.txt", encoding="UTF-8") as inputf, open("diary111.txt", "w", encoding="UTF-8") as outputf:
#     # sys.stdout = outputf
#     sys.stdin = inputf
#     t = sys.stdin.readlines()
#     # sys.stdout.write(sys.stdin.read())

# sys.stdout = sys.__stdout__
# sys.stdin = sys.__stdin__
# print(t)


def func(*args):
    return '-'.join(args)


with open("func.pkl", "wb") as f:
    pickle.dump(func, f)

with open('func.pkl', 'rb') as file:     # используется файл, полученный на предыдущем шаге
    obj = pickle.load(file)
    print(obj(*['1', '2']))
    print(type(obj))
