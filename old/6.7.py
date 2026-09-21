import sys
from collections import Counter
from functools import reduce

letters1 = Counter('earth')
letters2 = Counter('heart')

print(dict(letters1), letters2)


letters = Counter(set('Beautiful is better than ugly'))

print(letters['t'])

print()

files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
         'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
         'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
         'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
         'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
         'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
         'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
         'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
         'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
         'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
         'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
         'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
         'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
[print(f'{k}:', v) for k, v in sorted(
    Counter(map(lambda x: x.split('.')[1], files)).items())]

print()


def count_occurrences(word, words):
    l = Counter([i.lower() for i in words.split()])
    return (l[word.lower()])


word = 'Se'
words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'

print(count_occurrences(word, words))

print()

list_words = 'лимон,лимон,лимон,груша,банан,банан,киви,киви,киви,киви'
for k, v in sorted(Counter(list_words.split(',')).items()):
    print(f'{k}:', v)

print()


# for line in sys.stdin:
#     print(line.strip('\n'))

# data = [line.strip() for line in sys.stdin if line.strip() != 1]
# data = sys.stdin.readlines()
# print(data)


s = 'лимон,лимон,лимон,груша,банан,банан,киви,киви,киви,киви'
l = s.split(',')
m = max(map(lambda x: len(x), l))
for k, v in sorted(Counter(l).items()):
    s = reduce(lambda x, y:  x + ord(y) if ord(y) != ord(' ') else x, k, 0)
    print(f'{k.ljust(m)}: {s} US x {v} = {s*v}')

print(sum(map(ord, filter(str.isalpha, 'банан1'))))


def get_price(product):
    return sum(map(ord, filter(str.isalpha, product)))


print('-'*40)
cnt = Counter()
with open('pythonzen.txt', encoding='utf-8') as f:
    l = f.read()

for i in l:
    if i.isalpha():
        cnt.update(i.lower())
    # print(l)

for k, v in sorted(cnt.items()):
    print(f'{k}: {v}')


data = Counter(
    'aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.__dict__['min_values'] = lambda: sorted(filter(
    lambda x: x[1] == min(data.values()), data.items()))
data.max_values = lambda: sorted(filter(
    lambda x: x[1] == max(data.values()), data.items()))

print(data.min_values())
print(data.max_values())
