# '=========Число(int)========'
# # integers(int) - целые числа

# num = 10
# print(type(num)) # int

# # float - вещественное числа (с поавающей точкой, десятичные)

# num2 = 0.5
# print(type(num2)) # float
# print(float(num)) # 10.0 - int -> float
# print(int(num2)) # 0 - float -> int, без округление

# num3 = '0.5'
# num4 = float(num3)
# print(int(num4))
# num5 = 0.5
# print(str(num5)) # 0.5 -> '0.5'

# print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1) # 0.99999999

# deсimal - точное вещество число
# чтобы работать с Dtсimal его нужно импортироавать

# from decimal import Decimal

# num = '0.1'
# num2 = (Decimal(num))

# print(num2+num2+num2+num2+num2+num2+num2+num2+num2+num2)

'==============Операция над числами============='

5 + 7 # сложение
10 - 5 # вычитание
2 * 10 # умножение
50 / 10 # 5.0 деление
50 // 10 # 5 целочисленное деление
7 % 2 # 1 остаток от деления
5**2 # 25 возведение в степень
25**0.5 # 5 нахождения кв корня числа

# модуль числа  - из отрицательного числа делает положительное

# print(abs(-5)) # 5
# print(abs(10)) # 10
# print(abs(-0.5)) # 0.5

# # round - округление числа
# print(round(5.6)) # 6 (округление в большую сторону)
# print(round(5.5)) # 6
# print(round(5.4)) # 5
# print(round(5.49)) # 5 - округление идет только по первой цифле после точки

# # можно указать кол-во цифр аосле запятой
# print(round(5.49, 1))

# # sqrt - функция для нахождение кв корня числа
from math import sqrt

print(sqrt(25)) # 5
print(sqrt(81)) # 9

# # pow
# # 1. возводит цисло в степень
# # 2. находит остаток от деления на 3 число

print(pow(2, 5)) # 2 ** 5 = 32
print(pow(2, 5, 4)) # (2 ** 5) % 4 = 0

# # divmod - функция которая возвпащает 2 числа, где 1 - целая часть от деления, 2 - остаток от деления

# print(divmod(5, 2)) # 2, 1
# print(divmod(44, 3)) # 14, 2
