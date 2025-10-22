i = 3
for _ in range(10):
    a1 = _ % i
    a2 = _ // i
    print(_, a1+a2*i,  '%=', a1, type(a1), '//=', a2, type(a2))


writeln = print            # как в языке Pascal 😀

i = 2
x = 2.12344
writeln('Hello world!')
writeln('Python', round(2.12344, i))


def rnd(a):
    def rn(x):
        return round(x, a)
    return rn


f = rnd(a=i)

print(f(x))


func = (lambda x: x % 19 == 0 or x % 13 == 0)(38)

s = 'aA'
func1 = (lambda x: x[0] in s or x[-1] in s)('aaaaf')

print(func1)
