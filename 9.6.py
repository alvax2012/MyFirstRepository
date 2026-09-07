def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'],  'top_grade': max(grades['grades'])}


info = {'name': 'Timur', 'grades': [30, 57, 99]}

print(top_grade(info))


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    for i in range(step):


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)
