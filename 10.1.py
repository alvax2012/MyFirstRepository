# import test2

# print('000'


numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62,
           64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]

num_iter = iter(numbers)

for _ in range(len(numbers)-1):
    next(num_iter)
print(next(num_iter))


numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62,
           64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]

iterator = iter(numbers)
*t, last = iterator

print(last, type(t))
