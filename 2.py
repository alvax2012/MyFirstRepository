import random
import string

n = 7    # количество попыток
s = {0: 'Орел', 1: 'Решка'}
s = {0: 1, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
for _ in range(n):
    print(s[random.randrange(1, 7)])


# s = [i in range(n) if   random.randrange(0, 2)	== 0:
length = 5
i = random.randrange(0, 2)
s = [chr(random.randrange(65, 92)) if i == 1 else chr(
    random.randrange(97, 123)) for i in range(length)]
print(*s, sep='')

n = 7
s = set()

while len(s) < 7:
    s.add(random.randrange(1, 50))
s = list(s)
print(*sorted(s))


def generate_index():
    s = string.ascii_uppercase
    return f'{random.choice(s)}{random.choice(s)}{random.randrange(100)}_{random.randrange(100)}{random.choice(s)}{random.choice(s)}'


print(generate_index())

print('--'.join('asd'))

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
random.shuffle(matrix)
print(matrix)

n = string.digits
s = [[random.choice(n) if _ != 0 else random.randrange(1, 10)
      for _ in range(7)] for _ in range(3)]

for _ in s:
    print(*_, sep='')


s = [int(_) for _ in random.sample(string.digits, 6)]

s.insert(0, random.randrange(1, 10))
# print(s)
s = [random.sample(range(10), 7) for _ in range(3)]
print(s)

s = 'липа'
# s = list(s)
s = random.sample(s, len(s))
# random.shuffle(s)
print(''.join(s))
