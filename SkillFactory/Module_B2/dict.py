person = {} # с помощью фигурных скобок можно создать словарь

# словарь заполняется по принципу — ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}

# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}

my_dict = {}  # создание пустого словаря
my_dict

my_dict = dict()  # другой способ создания пустого словаря
my_dict

fruit_dict = {
    'Банан': '16 рублей',
    'Яблоко': '28 рублей',
    'Персик': '37 рублей',
    'Манго': '100 рублей',
    'Апельсин': '30 рублей'
}
print(fruit_dict)

fruits = ['Банан', 'Яблоко', 'Персик', 'Манго', 'Апельсин']
prices = ['16 рублей','28 рублей','37 рублей','100 рублей','30 рублей']
fruit_dict = dict(zip(fruits, prices))
print(fruit_dict)

user_dict = {
    'id': 532,
    'name': 'Ксения',
    'surmame': 'Собчак',
    'age': 40,
    'gender': 'female',
    'mail': 'sobchak@yandex.ru',
    'count_orders': 1402
}

values = list(user_dict.values())
print(values)
values = list(user_dict.keys())
print(values)
values = list(user_dict.items())
print(values)

user_dict = {
    'id': 532,
    'name': 'Ксения',
    'surmame': 'Собчак',
    'age': 39,
    'gender': 'female',
    'mail': 'sobchak@yandex.ru',
    'count_orders': 1402
}
#  user_dict['count_orders'] = user_dict['count_orders'] + 10
user_dict['count_orders'] += 10
user_dict['mail'] = 'ksobchak@mail.ru'
print(user_dict)

user_dict = {
    'id': 532,
    'name': 'Ксения',
    'surname': 'Собчак',
    'age': 39,
    'gender': 'female',
    'mail': 'sobchak@yandex.ru',
    'count_orders': 1402
}

new_name = 'Виктория'
new_surname = 'Боня'
login = '5GisEVIL'
password = 'BillGatesEVIL'
user_dict.update({
     'name': new_name,
     'surname': new_surname,
     'login': login,
     'password': password
     }
     )
print(user_dict)
