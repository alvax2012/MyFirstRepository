from datetime import datetime, date, time, timedelta
# mx = 475
# h1 = 1
# m1 = 55
# d = time(hour=1, minute=55)
# td = time(minute=mx)
# print(d, td, sep='\n')

# print(datetime.strptime(tt, '%Y%m%d'))  # .strftime('%d.%m.%Y'))

# a, b, c, d = 1, 2, 3, 4
# for i in range(a, b+1):
#     for j in range(c, d+1):
#         print('\t', (i, j), end='\t')
#     print()


s = 'acggtgttat'

print(100*(s.count('g')+s.count('c'))/len(s))

s = ''
l = sorted(filter(lambda x: s.count(str(x)) > 1, [
           int(i) for i in s.split()]))
l_out = []
for i in l:
    if i not in l_out:
        l_out.append(i)
print('=', *l_out)


n = 7

k = 0
for i in range(1, n+1):
    if k == n:
        print('==')
        break
    for j in range(i):
        print(i, end=' ')
        k += 1
    # print('k', k)

print(n)
