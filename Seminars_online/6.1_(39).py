# №6.1[39]. Даны два списка чисел. 
# Требуется вывести те элементы первого списка, которых нет во втором списке.

# Создайте функцию.
# Аргументы: два списка целых чисел
# Возвращает: список элементов (смотри условие)

# Примеры/Тесты:
# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [2, 3, 12]
# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3,4]

# [*] Усложнение. Элементы необходимо возвращать в том порядке, в котором они находятся в первом списке, с учетом повторений

# Примеры/Тесты:
# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [3, 3, 2, 12]
# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3, 4, 3, 4]


def diff_set(l: list, l_1: list) -> list:
    new_set = set(l).difference(set(l_1))
    return list(new_set)

print(diff_set([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))
print(diff_set([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5]))


# Через списки

def diff_list(l: list, l_1: list) -> list:
    result = []
    for element in l:
        if element not in l_1 and element not in result:
            result.append(element)
    return result

print(diff_list([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))
print(diff_list([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5]))