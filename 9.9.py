from functools import lru_cache

s = 'tutorial'


@lru_cache()
def eng_per(s):
    return ''.join(sorted(s))


print(eng_per(s))
