# Задача 1.3[6]. Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no

# (*) Усложнение. Вывод результат на экран сделайте одной строкой(только один print), для этого используйте тернарный оператор




number = int(input('Введите шестизначное число: '))

# Определяем сумму трех цифр справа:

discharge1 = number % 10
discharge2 = (number % 100) // 10
discharge3 = (number % 1000) // 100

rightSumOfDigits = discharge1 + discharge2 + discharge3

# Определяем сумму трех цифр слева:

discharge4 = (number % 10000) // 1000
discharge5 = (number % 100000) // 10000
discharge6 = (number % 1000000) // 100000

leftSumOfDigits = discharge4 + discharge5 + discharge6

# Сравниваем значения сумм слева и справа и выводим результат проверки

if rightSumOfDigits == leftSumOfDigits:
  print('YES')
else:
  print('NO')

# Сравнение и вывод результата с помощью тернарного оператора:

print('YES' if rightSumOfDigits == leftSumOfDigits else 'NO')
