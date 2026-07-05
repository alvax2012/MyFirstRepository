def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {func.__name__}")  # Код до вызова
        result = func(*args, **kwargs)          # Вызов оригинальной функции
        print(f"Функция {func.__name__} завершилась")  # Код после вызова
        t = True
        return result
    return wrapper


t = False


@log_decorator
def say_hello(name):
    return f"Привет, {name}!"


print(say_hello("Мир"))
