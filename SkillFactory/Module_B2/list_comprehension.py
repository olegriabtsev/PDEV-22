fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for i in fruits:
    if 'banana' != i:
        new_list.append(i)
    else:
        if 'banana' == i:
            new_list.append('orange')
print(new_list)
print('---')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x if x != 'banana' else 'orange' for x in fruits]
print(new_list)
print('---')

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
new_list = [x for x in fruits if "a" in x]
print(new_list)
print('---')

even_number = [x for x in range(1, 21) if x % 2 == 0]
print(even_number)
print('---')

squares = [x**2 for x in range(1, 11)]
print(squares)
print('---')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruit_tuples = [(fruit, len(fruit)) for fruit in fruits]
print(fruit_tuples)
print('---')

string = 'Hello World'
uppercase_letters = [letter for letter in string if letter.isupper()]
print(uppercase_letters)
