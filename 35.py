en = 'AaBCcEeHKMOoPpTXxy'

ru = 'АаВСсЕеНКМОоРрТХху'


s1, s2, s3 = 'Р', 'О', 'А'
l = (s1, s2, s3)
print(any(map(lambda x: x in en, l)))
