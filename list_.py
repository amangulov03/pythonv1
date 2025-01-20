'==============List============='
# списки - изменяемый, идексируемый, итерируемый тип данных предназначенный для хранения любых типов данных в определенном порядке

# list1 = [1, 2, 3, 2.6, [3, 4, 5], 'hi', True, False, None]
# print(list1[0])
# print(list1[4])
# print(list1[-4])
# print(list1[4][2])

# list2 = list('Hello World')
# print(list2) # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# print(list(range(1, 10)))
# range - это функция котороя создает последовательность
# range(start, end(не влючительно), step)

# print(list(range(0, 10, 2)))
# [0,1,2,3,4,5,6,7,8,9]
# [0, 2, 4, 6, 8]

# list2 = [1,2,3,4,5,6,7,8,9,10,11]
# print(list2)
# list2 = list(range(1, 12))
# print(list2)

'=================Методы списков=================='
# append - добовляет элемент в конец списка
# list3 = [9, 12, 'hi']
# list3.append(20)
# print(list3) # [20]
# list3.append('hi')
# print(list3) # [9, 12, hi, 20, hi]

# pop - удаляет элемент из мписка по индексу и возвращает удаленный элемент, ели индекс не указать то удаляет последний элемент
# list4 = ['h1', 'hello', 'katana']
# a = list4.pop(1)
# print(list4)
# print(a)

# remove - удаляет элемент из списка по значению
list6 = [12,25,6,7,5,6,9,4,61,69,2,3,23]
list6.remove(61)
print(list6)

list7 = [0,1,2,3,4,23,4,0,7,5,9,0]
count = list7.count(0)
print(count)

list7 = ['hello', 'hello', 'hello']
print(list7.count('l'))

# index - возвращает индекс первого вхождения принятого элемента

list8 = ['hi', True, False, 12, 'hi', 'good', 12, 1, 4, 0, 0, 1]
print(list8.index('hi', 2, 6))

# insert - доболяет элемент в список по индексу
list9 = ['hi', 12, True, False, 0]
list9.insert(1, 'hello')
print(list9)

# extend - доболяет элементы принятого списка в первый список, изменяя его
list1 = [1, 2, 3]
list2 = [0, 0, 0]
list1.append(list2) # [1, 2, 3, [0, 0, 0]]
list1.extend(list2) # [1, 2, 3 , 0, 0, 0]

list1.extend('str')
print(list1) # [1, 2, 3, [0, 0, 0], 0, 0, 0, 's', 't', 'r']

# list1.extend(123) # Error

# reverse - изменяет список растовляя его элементы в обратном порядке
list10 = [1, 2, 3, 4, 5, 6, 7, 8]
list11 = [1, 2, 3, 4, 5, [6, 7, 8]]
list10.reverse()
list11.reverse()
print(list10)
print(list11)

# sort - сортирует список, состоящей из элементов одгого типов данных
list12 = [23, 24, 1, 4, 0.5, 1, 0, 465, 3, 2, 56, 3, -4]
list12.sort()
print(list12)

list13 = ['a', 'v', ' ', 'hello', 'hi', 'abc', 'A', '-']
list13.sort()
print(list13)

list14 = [1, 2, 3]
list14.clear()
print(list14)

srt1 = 'hello'
lst1 = [1, 2, 3, 4, 5]
print(len(srt1))
print(len(lst1))


# a = 15
# b = 20

# a, b = [15, 20]

# name, age, prof = ['katana', 21, 'Dev']

# meshok = ['luk', 'kartoshka', 'ogurec', 'pomidor']

# for ruka in meshok:
#     print(ruka)

# list15 = [True, 'hi', 10, False, -5, 0.5, [1, 2, 3]]
# for i in list15:
#     print(i)

# итерация - процесс прохождения по элементам последовательности (итерируемого объекта)

# for i in 'hello world':
#     print(i.upper()* 5)

str1 = 'hello,world,name,age,12'
print(str1.split(',')) # str -> list

list17 = ['a', 'b', '12', 'c']
print(''.join(list17)) # list -> str

ls1 = [1, 2, 3]
ls2 = [1, 2, 3]

print(ls1 == ls2)
print(ls1 is ls2)
