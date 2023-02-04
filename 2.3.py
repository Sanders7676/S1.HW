# Задача 2.3[14]
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

# Примеры/Тесты:
# 10 ->
# 1
# 2
# 4
# 8

# (*) Усложнение. Вывод оформить в одну строку: числа выводить через запятую. Для этого воспользоваться параметрами функции print

# Примеры/Тесты:
# 10     -> 1,2,4,8,
# 10000  -> 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,


n = int(input(f'Введите число N: '))
current_power_of_two = 0
while 2**current_power_of_two <= n:
  print(2**current_power_of_two)
  current_power_of_two += 1
  # print(*(2**current_power_of_two), sep=', ')
  # или попробовать заменить 2**current_power_of_two на отдельную переменную.
