# 6.2[32]: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]

# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

print(' ')

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
num_1 = 2
# num_1 = 0
num_2 = 10
# num_2 = 9
# num_2 = 6

def create_list_2(list_1: int, num_1: int, num_2: int) -> None:
    list_2 = []
    for i in range(len(list_1)):
        if list_1[i] >= num_1 and list_1[i] <= num_2:
            list_2.append(i)
    print(list_2)

create_list_2(list_1, num_1, num_2)

print(' ')

# Формирование списка через Comprehension:
def create_list_2(list_1: int, num_1: int, num_2: int) -> None:
    print([i for i in range(len(list_1)) if list_1[i] >= num_1 and list_1[i] <= num_2])  # Принт с Компрехеншеном внутри

create_list_2(list_1, num_1, num_2)

print(' ')

# Формирование списка кортежей вида: индекс, значение
def create_list_2(list_1: int, num_1: int, num_2: int) -> None:
    print([(i, list_1[i]) for i in range(len(list_1)) if list_1[i] >= num_1 and list_1[i] <= num_2])  # Принт с Компрехеншеном внутри

create_list_2(list_1, num_1, num_2)

print(' ')