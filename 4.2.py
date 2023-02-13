# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом. 
# На входе задано количество ягод на каждом кусте. 
# Не обязательно вводить их с клавиатуры, можно задать непосредственно в коде программы.

# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7

# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1



# Задано количество ягод на каждом кусте - список / множество - list_1
# Вводим новый список с такой же длиной как список_1
# Циклом проходим по Списку_1 - по индексам!
# Припрохождении считаем сумму ягод на кусте по индексу и на двух соседних.
# Отдельно для индекса 0 считаем: инд.0 + инд.1 + инд.N
# Отдельно для инд. N считаем: инд.N + инд.N-1 + инд.0
# Полученные значения записываем в новый список.
# Находим максимальное значение для Списка 2 и показываем его индекс.


#find max value in list
# max_value = max(list_name)

#find index of max value in list 
# max_index = list_name. index (max_value)

# arrangement_of_bushes = [1, 2, 3, 4, 5, 6, 7, 8]
arrangement_of_bushes = [11, 92, 1, 42, 15, 12, 11, 81]

fee_for_approach = []

for bush in range(len(arrangement_of_bushes)):
    if bush == 0:
        fee_for_approach.append(arrangement_of_bushes[0] + arrangement_of_bushes[1] + arrangement_of_bushes[-1])
    elif bush == (len(arrangement_of_bushes) - 1):
        fee_for_approach.append(arrangement_of_bushes[-1] + arrangement_of_bushes[-2] + arrangement_of_bushes[0])
    else:
        fee_for_approach.append(arrangement_of_bushes[bush] + arrangement_of_bushes[bush - 1] + arrangement_of_bushes[bush + 1])

# print(fee_for_approach)

max_value_of_berry = max(fee_for_approach)

max_is_on_bush = fee_for_approach.index(max_value_of_berry) + 1

print(f'Макс. кол-во ягод {max_value_of_berry}, собрано для куста {max_is_on_bush}.')
