n, m = 4, 5
# n, m = [int(i) for i in input().split()]
mt = [[0]*m for _ in range(n)]


l = 1
ml = m
nl = n - 1

j0 = -1
i0 = 0
st = 1


if n < 2 or m < 2:
    t = 1
elif n == 2 or m == 2:
    t = 2
else:
    t = (m+n)//2

for k in range(t):
    col1 = j0 + st
    col2 = col1 + ml
    if st < 0:
        col2 = col1 - ml

    for j in range(col1, col2, st):
        mt[i0][j] = l
        l += 1
        j0 = j

    row1 = i0 + st
    row2 = row1 + nl
    if st < 0:
        row2 = row1 - nl

    for i in range(row1, row2, st):
        mt[i][j0] = l
        l += 1
        i0 = i

    ml -= 1
    nl -= 1
    st = - st

for row in mt:
    print(*[str(_).ljust(3) for _ in row])
