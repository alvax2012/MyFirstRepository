

total = 0

with open('diary.txt', encoding='utf-8') as file:
    for _ in file.readlines():
        total = total + 1

print(total)


def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char in vowels:
            char = char.upper()
        swapped_string += char

    return print(swapped_string)


print(swapcase_vowels('string'))


def get_max_index(numbers):
    return numbers.index(max(numbers))
