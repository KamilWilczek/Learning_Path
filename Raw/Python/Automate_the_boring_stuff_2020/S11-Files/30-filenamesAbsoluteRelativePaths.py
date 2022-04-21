print('c:\\spam\\eggs.png')
print(r'c:\spam\eggs.png')

print('\\'.join(['folder1', 'folder2', 'folder3', 'file.png']))

import os

# os.path.join(['folder1', 'folder2', 'folder3', 'file.png'])

# current working directory
print(os.getcwd())

# change working directory
os.chdir('d:\\')
print(os.getcwd())

# absolute paths:
# c:\bacon\fizz\spam.txt

# relative paths:
# .\fizz\spam.txt
# ..\eggs\spam.txt

os.chdir(r'D:\Kursy\Automate the boring stuff\S11-Files')
print(os.getcwd())

print(os.path.abspath('spam.txt'))
print(os.path.abspath('..\\..\\spam.txt'))
print(os.path.isabs('..\\..\\spam.txt'))
print(os.path.isabs('d:\\folder\\folder'))

print(os.path.relpath('d:\\folder1\\folder2\\spam.txt', 'd:\\folder1'))
print(os.path.dirname('d:\\folder1\\folder2\\spam.txt'))
print(os.path.basename('d:\\folder1\\folder2\\spam.txt'))

print(os.path.exists('d:\\folder1\\folder2\\spam.txt'))
print((os.path.exists('c:\\windows\\system32\\calc.exe')))

print(os.path.isfile('d:\\folder1\\folder2'))
print(os.path.isfile('c:\\windows\\system32\\calc.exe'))
print(os.path.isdir('D:\\Kursy\\Automate the boring stuff\\S11-Files'))
print(os.path.isdir('c:\\windows\\system32\\calc.exe'))

print(os.path.getsize('c:\\windows\\system32\\calc.exe'))

print(os.listdir('D:\\Kursy\\Automate the boring stuff\\temp'))

totalSize = 0
for filename in os.listdir('D:\\Kursy\\Automate the boring stuff\\temp'):
    if not os.path.isfile(os.path.join('D:\\Kursy\\Automate the boring stuff\\temp', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('D:\\Kursy\\Automate the boring stuff\\temp', filename))

print(totalSize)

os.makedirs('D:\\Kursy\\delicious\\walnut\\waffles')
os.removedirs('D:\\Kursy\\delicious\\walnut\\waffles')

