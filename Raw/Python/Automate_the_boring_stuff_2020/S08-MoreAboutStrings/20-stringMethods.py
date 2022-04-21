spam = 'Hello world!'
print(spam.upper())

spam = spam.upper()
print(spam)

print(spam.lower())

print(spam.islower())
print(spam.isupper())

print('Hello'.upper().isupper())

print('hello'.isalpha())
print('hello123'.isalpha())
print('hello1223'.isalnum())
print('123'.isdecimal())
print('    '.isspace())
print('Hello world!'[5].isspace())
print('This Is Title Case.'.istitle())
print('Hello world!'.title())

print('Hello world!'.startswith('Hello'))
print('Hello world!'.startswith('H'))
print('Hello world!'.startswith('ello'))
print('Hello world!'.endswith('wold!'))
print('Hello world!'.endswith('wold'))

print(','.join(['cats', 'rats', 'bats']))
print('\n\n'.join(['cats', 'rats', 'bats']))

print('My name is Simon'.split())
print('My name is Simon'.split('m'))

print('Hello'.rjust(10))
print('world!'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.center(20, '='))

print('Hello'.rjust(10).strip())
print('    x     '.strip())
print('    x     '.lstrip())
print('    x     '.rstrip())
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))

spam = 'Hello there!'
print(spam.replace('e', 'XYZ'))

import pyperclip

pyperclip.copy('Hello!!!!!!')
print(pyperclip.paste())

