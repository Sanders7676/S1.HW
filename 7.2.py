# 6.2[32]: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, 
# т.е. функцию двух аргументов. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.

# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
# 1   1   1   1
# 2   4   8  16
# 3   9  27  81
# 4  16  64 256

# print_operation_table(lambda x,y: x*y)
# 1   2   3   4   5   6
# 2   4   6   8  10  12
# 3   6   9  12  15  18
# 4   8  12  16  20  24
# 5  10  15  20  25  30
# 6  12  18  24  30  36

# print()

# def operation1(row, column):
#     return row * column

# def operation2(row, column):
#     return row ** column

# operation = lambda row, column: row * column
# print(operation(2, 2))

print()

def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for row in range(1, num_rows + 1):
        # rows = []
        # for column in range(1, num_columns + 1):
        #   element = operation(row, column)
        #   rows.append(element)
        # print(*rows)
        print(*[operation(row, column) for column in range(1, num_columns + 1)])     # Компрехеншен

# print_operation_table(operation1, 4, 4)
# print()
# print_operation_table(operation2, 4, 4)
print()
print_operation_table(lambda x,y: x**y,4,4)
print()
print_operation_table(lambda x,y: x*y)
print()

# (*) Усложнение. Сформируйте форматированный вывод с номерами строк и столбцов

# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
#        1   2   3   4
#     ----------------
# 1 |    1   1   1   1
# 2 |    2   4   8  16
# 3 |    3   9  27  81
# 4 |    4  16  64 256

# print_operation_table(lambda x,y: x*y)
#        1   2   3   4   5   6
#     ------------------------
# 1 |    1   2   3   4   5   6
# 2 |    2   4   6   8  10  12
# 3 |    3   6   9  12  15  18
# 4 |    4   8  12  16  20  24
# 5 |    5  10  15  20  25  30
# 6 |    6  12  18  24  30  36
