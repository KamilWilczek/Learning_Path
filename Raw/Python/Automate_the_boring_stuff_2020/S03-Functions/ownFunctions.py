# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')


def hello(name):
    print('Hello ' + name)


hello('Alice')
hello('Bob')


def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

print('Hello', end='')
print('World')

print('cat', 'dog', 'mouse', sep='ABC')