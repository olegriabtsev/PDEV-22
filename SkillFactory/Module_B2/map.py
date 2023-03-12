string = input('Add numbers with a space: ')
print(type(string))
print(string)

list_of_strings = string.split()
print(type(list_of_strings))
print(list_of_strings)

list_of_numbers = list(map(int, list_of_strings))
print(sum(list_of_numbers[::3]))
