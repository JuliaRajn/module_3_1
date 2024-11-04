calls = 0

def count_calls():
  """
  Функция для подсчета вызовов других функций.
  """
  global calls
  calls += 1


def string_info(string):
  """
  Функция, принимающая строку и возвращающая кортеж из:
  длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
  """
  count_calls()
  return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
  """
  Функция, принимающая строку и список, и возвращающая True,
  если строка находится в этом списке, False - если отсутствует.
  Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
  """
  count_calls()
  string = string.upper()
  return string in [item.upper() for item in list_to_search]

# Вызовы функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

# Вывод количества вызовов
print(calls)
