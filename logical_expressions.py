'=======Логические и условные операторы======='
# логическое операторы - выражения, которые возвращают True, если выражение верное, False - если выражение не верное

'Равенство'
10 == 5 # False
5 == 5 # True
# print('hi' == 2)
'he' == 'hi' # True
'He' == 'hi' # False
'5' == 5 # False
'+' == '+' # True

'Не равенство'
4 != 5 # True
5 != 5 # False

'Больше'
10 > 10 # False
4 > 1 # True

'Меньше'
5 < 4 # False
10 < 10 # False

'Больше или равно'
10 >= 4 # True
10 >= 10 # True
4 >= 5 # False

'Меньше или равно'
10 <= 10 # True
5 <= 10 # True
10 <= 5 # False

'===============Abd Or Not================'
# and - и
# or - или
# not - не

a = 5
b = 6
# True  и   True
a == 5 and b == 6 # True

# False  и   True
a == 7 and b == 6 # False

# False  и  True
a > 10 and b <= 6 # False

# False  и  False
a == 0 and b == 0 # False

# ечли все части выражения вохвпащают True - будет True
# есди хотя бы одна часть выпажения False - будет False


# True или  True
a == 5 or b == 6 # True

# False или  True
a > 10 or b == 6 # True

# True или  False
a < 20 or b == 10 # True

# False или False
a == 1 or b == 1 # False

# ечли хотя бы одна часть выражения True - будет True


# not True -> False
# not False -> True

    # True
not a == 5 # False

not a < 20 or not b == 6 # False

# print(not b > 20 and a == 5 or b == 6 or a < 6 and b >= 6 or not a == 5 and 5 == 10)


'===============Boolean type=================='
# Булевый тип данных имеет всего 2 значения True и False

bool(1) # True
bool(-12) # True
bool(0) # False

bool("hello") # True
bool(" ") # True
bool("_") # True
bool("") # False

bool(True) # True
bool(False) # False


'===========NoneType=========='
# None - неизменяемый тип данных с одним значением None, который используется для обозначения отсутствия значения

# a = None

# bool(None) # False

a = 5
b = 5
print(a is b)


'==================Условные операторы===================='
# Условные операторы - конструкция, которая используется для того, чтобы при разных данных код работал по разному (в зависимости от условия)

# if условие1:
#     действие1

pogogda = input("Введите погоду: ")
if pogogda == "солнечно":
    print("Взять солнц-очки")
elif pogogda == "дождливо":
    print("Взять зонтик")
else:
    print("Ошибка")

'==============Тернарный оператор==============='
# Тернарный опреатор - условие в одну строку

num = 23
if num > 0: # условие1
    int_ = "положитнльное" # действие1
else:
    int_ = "отрицательное" # действие2
# обычный условие

        # действие1  условие1           действие2
int_ = "положитнльное" if num > 0 else "отрицательное"
# тернарное условие (оператор)
