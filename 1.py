from collections import Counter


def get_price(product):
    return sum(map(ord, filter(str.isalpha, product)))


s = 'МаЛиНа клубника Арбуз банаН Малина Черешня вишня арбуз клубника банан'.lower().split()
cnt1 = Counter(s)
cnt1 = Counter({'b': 8, 'a': 2, 'c': 3})
most_common_word = max(cnt1, key=lambda x: (cnt1[x], x))
print(most_common_word)
