def hide_card(s: str):
    s1 = '*' * 12 + s.replace(' ', '')[-4:]
    return s1, len(s1)


card = '3456 9012 5678 1234'
print(hide_card(card)[0])
