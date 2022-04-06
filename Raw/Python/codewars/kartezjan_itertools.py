from itertools import permutations
from itertools import product

input_data = {
    "szerokość": {"20cm", "16cm", "10cm"},
    "wysokość": {"30cm", "40cm"},
    "kolor": {"czarny", "biały", "zielony"},
}

# input_data = {
#     ["szerokość"]: ["20cm", "16cm", "10cm"],
#     ["wysokość"]: ["30cm", "40cm"],
#     ["]kolor"]: ["czarny", "biały", "zielony"],
# }

# perm = permutations(input_data.values())
# for i in list(perm):
#     print(i)

# a = product(input_data.values())
# for i in a:
#     print(i)

# print(input_data["szerokość"])
# for i in input_data["szerokość"]:
#     print(i)

# store = {}
# for key, value in input_data:
#     store.setdefault(key, set()).add(value)
# print(store)

"""
lista = [
    {'key1': 'set1key1', 'key2' :'set1key2', key3 : set1key3},
    {'key1': 'set2key1', 'key2' :'set2key2', key3 : set2key3},
]
"""
