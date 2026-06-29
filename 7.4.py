from sys import exc_info
import sys


print(issubclass(IndexError, LookupError))
print(issubclass(LookupError, IndexError))

try:
    nums = [10, 5, 20, 25]
    print(nums[100])
except BaseException as err:    # записываем сгенерированное исключение в переменную err
    print(err)
    print(type(err))


try:
    х = 1 / 0
except Exception as err:
    print(exc_info())

# while True:
#     print(input())

# data = sys.stdin.read()
# print(data)

for line in sys.stdin:
    print(line.strip('\n'))
