import sys
from datetime import datetime, date, time, timedelta
# i = 0
# for line in sys.stdin:
#     i += 1
#     print(f'{i}=', line.strip('\n'))

# print('=', sys.stdin.readlines())


# name, surname = input()

# print(name, surname)


# [print(i) if i.strip('\n') != '11' else print(chr(26)) for i in sys.stdin]

# temp = sys.stdin

# sys.stdin = open("diary111.txt", encoding="UTF-8")
# n = input()
# for i in range(2):
#     print(input())

# sys.stdin.close()
# sys.stdin = temp

# s = '1'
# while s != '11':
#     s = sys.stdin.readline().strip('\n')
#     print(type(s), s, '--')


# f = open("diary111.txt", encoding="UTF-8")
# s = f.readlines()
# print(s)
# f.close()

# with open("diary.txt", encoding="UTF-8") as inputf, open("diary111.txt", "w", encoding="UTF-8") as outputf:
#     # sys.stdout = outputf
#     sys.stdin = inputf
#     t = sys.stdin.readlines()
#     # sys.stdout.write(sys.stdin.read())

# sys.stdout = sys.__stdout__
# sys.stdin = sys.__stdin__
# print(t)
# print('-'*10)

# with open("diary1112.txt", encoding="UTF-8") as f:
#     s = f.readlines()
# print(s)


# l = ['s = str(input())\n', 'k = 0\n', '#подсчитываем количество цифр\n', 'for i in range(len(s)):\n', '    #проверяем каждый символ\n',
#      "    if s[i] in '0123456789': #проверяем, является ли элемент строки цифрой\n", '        k += 1\n', 'print(k)']

# print(len(list(filter(lambda x: x[0] == '#', map(lambda x: x.strip(), l)))))


# *a, b = [1, '2', '937']
# print(a, b)

# z = a.pop()
# print(z[0])


# l = [datetime.strptime(i, '%d.%m.%Y') for i in sys.stdin]
# print(l)


# i = 0
# for line in sys.stdin:
#     i += 1
#     print(f'{i}=', line.strip('\n'))

# print('=', list(sys.stdin.readline()))

print(list(input()))
