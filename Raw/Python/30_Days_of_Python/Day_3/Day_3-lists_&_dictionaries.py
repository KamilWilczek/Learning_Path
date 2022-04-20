my_cart = [12.99, 312, 32, 142]
sum(my_cart)

my_cart.append(39.99)
print(my_cart)

len(my_cart)

print(my_cart[2])
my_cart[2] * 120

my_string = "hello world"
len(my_string)
my_string[4]

my_items = ["mouse", "laptop", "mic", "screen", "snack"]
my_products = [my_cart, my_items]

# ------------------------------------------------------------
#  dict ={key:value, key1:value1}
my_data = {"name": "Justin Mitchel", "location": "California"}
my_data["name"]
# my_data[0] -> error
my_data.keys()
list(my_data.keys())
list(my_data.keys()[0])
# my_data.append({'occ':'coder'}) -> error
my_data["occ"] = "coder"
print(my_data)

user_1 = {"name": "James Bond"}
user_2 = {"name": "Ned Stark"}
my_users = [user_1, user_2]
print(my_users)
