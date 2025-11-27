en = 'AaBCcEeHKMOoPpTXxy'

ru = 'АаВСсЕеНКМОоРрТХху'


s1, s2, s3 = 'Р', 'О', 'А'
l = (s1, s2, s3)
if all(map(lambda x: x in en, l)):
    print('en')
elif all(map(lambda x: x in ru, l)):
    print('ru')
else:
    print('mix')

langs = ['ru', 'mix', 'mix', 'en']
eng = 'AaBCcEeHKMOoPpTXxy'
ind = sum(_ in eng for _ in l)
print(*(_ in eng for _ in l))
print(langs[ind])
