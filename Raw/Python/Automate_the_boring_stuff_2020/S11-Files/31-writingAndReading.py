helloFile = open('D:\\Kursy\\Automate the boring stuff\\S11-Files\\hello.txt')
print(helloFile.read())
helloFile.close()

helloFile = open('D:\\Kursy\\Automate the boring stuff\\S11-Files\\hello.txt')
content = helloFile.read()
print(content)
helloFile.close()

helloFile = open('D:\\Kursy\\Automate the boring stuff\\S11-Files\\hello.txt')
print(helloFile.readlines())
helloFile.close()

# 'w' - write mode and overwrite
# 'a' = append mode, no overwrite
# in this cases if file does not exist python will create blank file

helloFile = open('D:\\Kursy\\Automate the boring stuff\\S11-Files\\hello2.txt', 'w')
helloFile.write('Hello!!!!!!!')
helloFile.write('Hello!!!!!!!')
helloFile.write('Hello!!!!!!!')
helloFile.close()

baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')
baconFile.close()

import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile.keys())
print(list(shelfFile.keys()))
print(list(shelfFile.values()))


