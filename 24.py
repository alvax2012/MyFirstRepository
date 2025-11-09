s = 'stepik.txt'
with open("forbidden_words.txt", encoding="utf-8") as file, open(s) as infile:
    text = infile.read()
    for f in file.read().strip("\n").split():
        pos = text.lower().find(f)
        while pos > -1:
            text = text[:pos] + "*" * len(f) + text[pos+len(f):]
            pos = text.lower().find(f)
print(text)
