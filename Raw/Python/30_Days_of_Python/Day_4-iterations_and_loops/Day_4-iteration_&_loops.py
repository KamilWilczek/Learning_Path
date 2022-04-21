my_list = [1, 2, 3, 4, 5]
my_list[0]
my_list[1]
my_list[2]
my_list[3]
my_list[4]
for my_var in my_list:
    print(my_var)
print(my_var)

# for x in 10:
#     print(x) -> error

for x in "10":
    print(x)

for x in range(10):
    print(x)

user_1 = {"username": "jmitchel3", "id": 1}
user_2 = {"username": "abc", "id": 2}
my_users = [user_1, user_2]
for user in my_users:
    print(user)

for user in my_users:
    print(user["username"])

# for user in my_users:
#     print(user["email"]) -> error

user_1 = {"username": "jmitchel3", "id": 1}
user_2 = {"username": "abc", "id": 2, "email": "abc@abc.abc"}

# for user in my_users:
#     print(user["email"]) -> error

for user in my_users:
    if "email" in user:
        print(user["email"])

selected_user = {}
my_user_lookup = 2
for user in my_users:
    if "id" in user:
        if user["id"] == my_user_lookup:
            selected_user = user
print(selected_user)

for x in range(0, 10):
    print(x)

for x in range(0, 10):
    for users in my_users:
        if user["id"] == x:
            print(user)
