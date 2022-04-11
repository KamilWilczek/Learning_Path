if True:
    print("hi there")

if False:
    print("nothing")

if not False:
    print("what's up?")

print(True == False)
print(10 > 32)
print(424 < 323433)
print(10 > 32 or 10 < 32)
print(not 10 > 32)
print(not (10 > 32))
print(200 > 200)
print(200 >= 200)
print(200 > 200 or 200 == 200)

str(True).lower() == "true"
str("true").title() == "True"
str("true")
"abc".title()
bool(str("true").title())

abc = [1, 2, 3, 4, 5]
abc_sq = []
for num in abc:
    new_number = num**2
    abc_sq.append(new_number)
print(abc_sq)

is_even = []
is_odd = []
for num in abc_sq:
    if num % 2 == 0:
        print("This is even")
        is_even.appned(num)
    else:
        is_odd.append(num)
print(is_even, is_odd)

is_factor_of_3 = []
for num in abc_sq:
    if num % 3 == 0:
        is_factor_of_3.append(num)
    elif num % 2 == 0:
        is_even.appned(num)
    else:
        is_odd.append(num)
print(is_factor_of_3)
print(is_even, is_odd)

for num in abc_sq:
    if num % 3 == 0:
        is_factor_of_3.append(num)
    else:
        if num % 2 == 0:
            is_even.appned(num)
        else:
            is_odd.append(num)


x = 10
i = 0
while i < x:
    print(i)
    i = i + 1

x = 10
i = 0
z = 12
while i < x:
    z = z * 2
    if z > 342900:
        break
    print(z, i)
    i = i + 0.00000001

x = 10
i = 0
while i < x:
    if i % 2 == 0:
        print("event")
    else:
        continue
    i += 1

x = 10
i = 0
while i < x:
    if i % 2 == 0:
        continue
    else:
        print("odd")
        i += 1

x = 10
i = 0
while i < x:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
