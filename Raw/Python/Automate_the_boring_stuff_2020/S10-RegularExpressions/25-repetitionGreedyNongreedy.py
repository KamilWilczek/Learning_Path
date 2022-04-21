import re

# ? - zero or one
# * - zero or more
# + - one or more
# {3} - exactly 3

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo == None)

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo == None)

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo.group())
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman')
print(mo == None)
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())

regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? regex syntax'))
regex = re.compile(r'(\+\*\?)+')
print(regex.search('I learned about +*?+*?+*? regex syntax'))

haRegex = re.compile(r'(Ha){3}')
print(haRegex.search(' He said "HaHaHa"'))
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}')
print(phoneRegex.search('My numbers are 415-555-1234, 555-4242, 212-555-0000'))

haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search(' He said "HaHaHaHa"'))
print(haRegex.search(' He said "HaHaHaHaHaHaHaHa"'))
# haRegex = re.compile(r'(Ha){,5}') # {0,5}
# haRegex = re.compile(r'(Ha){3,}') # {3, or more}


# matches longest possible match - greedy
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890'))

# matches shortest possible match - Nongreedy
digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('1234567890'))




