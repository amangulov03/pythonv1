'=================Exceptions==============='
# Исключения - объекты, которые прерывают работу кода, если они не оброботаны

# Ошибки -объекты, которые прерывают работу кода, но их нельзя оброботать, не считая исключения

IndexError
# исключения, которое выводит, когда мы обращаемся по несуществующему индексу

'''
list_1 = [23, 15, 4, 2]
list_1[1000]
'IndexError: list index out of range'
'''

'''
list_2 = [12, 23, 2, 1]
list_2.pop(1000)
'IndexError: pop index out of range'
'''
'''
list_3 = []
list_3.pop()
IndexError: pop from empty list
'''


KeyError
# исключения, которое выходит, когда обращаемся по несуществующему ключу

'''
dict_1 = {'a': 1}
dict_1['b']
KeyError: 'b'
'''


ValueError
# когда мы передаем в функцию не коректный для нее тип данных
# когда мы распаковываем итерируемый объект на несколько переменных и кол-во перменных не совподает и ккол-во элементов в итерируемом объекте

'''
int('10b')
ValueError: invalid literal for int() with base 10: '10b'
'''

a = 1
b = 2
c = 3

'''
a, b, c, = [1, 2, 3, 6]
ValueError: too many values to unpack (expected 3)
'''


TypeError
# кргда мы пытаемся использовать метод не свойственный какому-то типу данных
# когда мы пытаемся передать функции больше или меньше фргументов, чем принимает функция

'''
for i in 123456789:
    ...
TypeError: 'int' object is not iterable
'''

'''
5 + '5'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

'''
'5' + 5
TypeError: can only concatenate str (not "int") to str
'''

'''
{[1, 2, 3]: 'hello'}
TypeError: unhashable type: 'list'
'''

'''
input('enter', 2)
TypeError: input expected at most 1 argument, got 2
'''

'''
[].append()
TypeError: list.append() takes exactly one argument (0 given)
'''


ZeroDivisionError
# выходит при делении на 0

'''
45 / 0
ZeroDivisionError: division by zero
'''

'''
45 // 0
ZeroDivisionError: integer division or modulo by zero
'''

'''
45 % 0
ZeroDivisionError: integer modulo by zero
'''

AttributeError
# выходит когда мы обращаемся несуществующему атрибуту или методу объекта (типы данных)


'''
[].replace('', 'a')
AttributeError: 'list' object has no attribute 'replace'
'''

'''
''.pop()
AttributeError: 'str' object has no attribute 'pop'
'''

SyntaxError
'''
my num = 56
SyntaxError: invalid syntax
'''

'''
a =
SyntaxError: invalid syntax
'''


IndentationError
# исключение которое выходит, когда мы используем неправильные отступы
'''
    num = 15
IndentationError: unexpected indent
'''

'''
for i in range(11):
print(i)
IndentationError: expected an indented block after 'for' statement on line 142
'''

NameError
# исключение, которое выходит когда мы обращаемся к несуществующей переменной
'''
num1 = 15
print(num2)
NameError: name 'num2' is not defined. Did you mean: 'num1'?
'''

Exception
# исключение, которе создали, чтобы его вызывать

'==================Вызов Исключений=================='
# raise NameError("Я вызвал неймерор просто так")

'==================Оброботка исключений====================='
# чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except, и обробатывать вызовное исключение

# try:
#     # код, который возможно вызовет ошибку
#     num = int(input("Введите число: "))
# except ValueError:
#     # Код который, отрабатывает только если ошибка вызывалась
#     print("Вы ввели не число")
# else:
#     # Код который, отрабатывает только если никакая ошибка не вышла
#     print("Вы ввели число")
# finally:
#     print("До свидания!")


# try:
#     raise  NameError
# except (AttributeError, ValueError):
#     print('Вышла ошибка - AttributeError или ValueError')

# try:
#     raise ZeroDivisionError
# except:
#     print('hi')


# try:
#     raise ZeroDivisionError
# except Exception:
#     print('hi')


# try:
#     raise ValueError
# except ValueError:
#     print('Вышел ValueError')
# except TypeError:
#     print('Вышел TypeError')

# try:
#     password = input("Введите пароль: ")
#     if password == "hello123":
#         print("Вы в системе")
#     elif password != "hello123":
#         raise Exception("Вы ввели пароль не верно!")
# except Exception as e:
#     print(e)


try:
    print(11)
finally:
    print('hi')
