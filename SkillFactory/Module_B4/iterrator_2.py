def my_animal_gen():
    yield 'cow'
    print('---')
    for animal in ['cat', 'dog', 'bear']:
        yield animal
        print('---')
        yield 'whale'


var = my_animal_gen()
print(next(var))
print(next(var))
print(next(var))

for i in var:
    print(i)
