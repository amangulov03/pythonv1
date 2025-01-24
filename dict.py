'=====================Dict(словари)==================='
# dict - это изменяемый, итерируемый, 'неупорядоченный', индексируемых тип данных, для хранения данных в парах (ключ:значение)

# user = {
#     'name': 'Katana',
#     'age': 21,
#     'prof': 'Dev'
#     }

# print(user['name']) # Katana

# ключами в словоре могут быть только неизменяемые типы данных
# если в словоре есть одинаковые ключи то сохрпнится последние

# dict1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'a': 4
#     }
# print(dict1) # {'a': 4, 'b': 2, 'c': 3}

# print(dict1['f']) # KeyError 'f'

'====================Создание======================='
# user = {'a': 1, 'b': 2}

# user = dict([('a', 1), ('b', 2), ('c', 3)])

# tuple1 = ()
# list1 = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# dict1 = dict(list1) # {'a': 'b', ...}

# dict1 = {'prof': 'dev'}
# dict1['name'] = 'Katana'
# dict1['age'] = 21
# dict1['prof'] = 'artist'
# # {'prof': 'artist', 'name': 'Katana', 'age': 21}


'================Методы словаря==============='

# # get - метод, который возвращает значение по ключу, если такого ключа нет, то возвращает None или дефолтное значение
# user = {
#     'name': 'katana',
#     'age': 21,
#     'prof': 'dev'
# }
# print(user.get('nameывыв', 'Такого ключа нет')) # Такого ключа нет

# # pop - удаляет пару по ключу и возвращает значение
# num = user.pop('age') # 21
# print(num)

# # popitem - удаляет последнюю пару и возвращает её
# dict1 = {
#     'a': 1,
#     'b': 2
# }
# num = dict1.popitem() # {'b', 2}
# print(num)

# # update - расширяет словарь парами из второго словоря
# dict1 = {
#     1: 'a',
#     2: 'b'
# }
# dict2 = {
#     3: 'c',
#     4: 'd'
# }
# dict1.update(dict2)
# print(dict1) # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# print(dict2) # {3: 'c', 4: 'd'}

# # fromkeys - метод для создания нового словоря, используя список ключей
# dict1 = dict.fromkeys('hi', 12)
# print(dict1)

dict2 = dict.fromkeys([1, 2, 3], "hello")
print(dict2)



# dict1 = {1: 'a', 2: 'b'}
# # keys - возвращает все ключи - dict_keys([1, 2])
# # values - возвращает все значения - dict_values(['a', 'b'])
# # items - возвращает все пары - dict_items([(1, 'a'), (2, 'b')])
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

'=================Итерирование словарей================='
# user = {
#     'name': 'katana',
#     'age': 21,
#     'prof': 'dev'
# }

# for key, values in user.items(): # ('nmae', 'katana')
#     print(key, values)

# вам дан словарь
# создайте новый словарь, поменяв ключи со сзначениями
# dict2 = {1: 'a', 2: 'b', 3: 'c'}

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {}
# for key, values in dict1.items():
#     dict2.update({values: key})
# print(dict2)

print(dir(dict()))
print(dir(dict()))
print(dir(dict()))

# Словари Python позволяют хранить данные в формате "ключ: значение".
# Метод .items() позволяет получить пары из словаря для обработки.
# Метод update удобно добавляет новые пары в словарь.
# Таким образом, с помощью простого цикла и метода update мы инвертируем словарь.
