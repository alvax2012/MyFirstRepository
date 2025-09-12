import random

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
