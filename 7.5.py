try:
    1 / 0
except ZeroDivisionError as e:
    raise
  # Плохо! Теряется исходный стек
