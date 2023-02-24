# №7.1[###]. Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич

# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович

# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# [*] Усложнение. Файл находится в поддиретории data текущей директории. Сформировать путь к нему с использованием
# os.path и pathlib


lst = [['Иванов', 'Иван', 'Иванович'],
['Петров', 'Петр', 'Петрович'],
['Соколов', 'Илья', 'Григорьевич'], ]


def template1(man):
surname, name, parent = man
return f"{surname}-{name[0]}-{parent[0]}"


def filter1(man):
surname, name, parent = man
if surname[0] == "П": return True
return False