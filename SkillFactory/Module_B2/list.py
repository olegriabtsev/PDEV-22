s = [0, 'hello', (1, 'a')]
print(s)

letters = ['a', 'b', 'c', 'd']
letters.append('e')
letters.append('f')
letters.append('g')
print(letters[1:4])
print(len(letters))
print(letters[len(letters)-1])
print(letters[-1])
print(letters[-4])
print(letters[::-1])

letters.pop(3)
print(letters)

array_of_arrays = [
    [1, 2, 3],
    [4, 5, 6],
    
    [7, 8, 9]
]
print(array_of_arrays[2])

array = [
    [0]*3,
    [0]*3,
    [0]*3
]
print(array)
array[0][0] = 2**0.5
array[1][1] = 2**0.5
array[2][2] = 2**0.5
print(array[0])
print(array[1])
print(array[2])

new_list = ['apple', 'orange', 'grape']
fruit = 'melon'
if fruit in new_list:
    print(f'Yes, {fruit} in the list ')
else:
    print(f'No, there is no {fruit} in the list')