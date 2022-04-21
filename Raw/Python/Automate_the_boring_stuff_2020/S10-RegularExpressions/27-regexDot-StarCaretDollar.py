import re

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('He said "Hello!"'))

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
print(endsWithWorldRegex.search('Hello world!safaffasf'))

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('213124235254423423'))
print(allDigitsRegex.search('2131242352x54423423'))


atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))



text = 'First Name: Al Last Name: Sweigart'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(text))

serve = '<To serve humans> for dinner.>'
nonGreedy = re.compile(r'<(.*?)>')
print(nonGreedy.findall(serve))
greedy = re.compile(r'<(.*)>')
print((greedy.findall(serve)))

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)
dotStar = re.compile(r'.*')
print(dotStar.search(prime))
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))
vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))

