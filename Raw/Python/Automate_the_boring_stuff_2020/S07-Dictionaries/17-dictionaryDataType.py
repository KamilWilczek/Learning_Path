myCat = {'size': 'fat',
         'color': 'gray',
         'disposition': 'loud'}

print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

spam = {12345: 'Luggage combintation',
        42: 'The Answer'}

eggs = {'name' : 'Zophie',
        'species': 'cat',
        'age' : 8}

ham = {'species' : 'cat',
       'name' : 'Zophie',
       'age' : 8}

print([1,2,3] == [3,2,1])
print(eggs == ham)

print('name' in eggs)
print('name' not in eggs)

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))
print(eggs.keys())

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

print(eggs.get('age', 0))
print(eggs.get('color', ''))

picnicItems = {'apples' : 5,
               'cups' : 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic.')

print(eggs)
eggs.setdefault('color', 'black')
print(eggs)
eggs.setdefault('color', 'orange')
print(eggs)

message = "It was bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
