spam = 42 # global scope


# def eggs():
#     spam = 42 # local scope


def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)


eggs = 42
spam()

print('Some code here.')
print('Some more code here.')