import sys
a = int('10111', 2)
b = int('01101', 2)
c = int('100100', 2)
d = int('000001', 2)
d1 = int('100101', 2)
print(a, b, c, d, d1)

# try:
#     while True:
#         line = input()
#         # обрабатываем строку
# except EOFError:
#     print("Был отправлен EOF (Ctrl+D или Ctrl+Z)")

for l in sys.stdin:
    print(l)
