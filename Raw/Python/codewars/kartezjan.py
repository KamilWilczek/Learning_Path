from itertools import product

input_data = {
    "szerokość": {"20cm", "16cm", "10cm"},
    "wysokość": {"30cm", "40cm"},
    "kolor": {"czarny", "biały", "zielony"},
}

# input_data = {
#    key    value
#     'key1': {'set'},
#     'key2': {'set'},
#     'key3': {'set'},
# }

# empty_dict = {}
# lista_kluczy = []
# lista_slownikow = []
# lista_list = []
# i = 0

# for key, value in input_data.items():
#     lista_kluczy.append(key)
#     lista_wartosci = []
#     for x in input_data[key]:
#         lista_wartosci.append(x)
#     lista_list.append(lista_wartosci)

# print("lista_kluczy", lista_kluczy)
# print("lista_list", lista_list)
# while i < len(lista_kluczy):
#     empty_dict[lista_kluczy[i]] = lista_list[0][0]
#     i = i + 1
# print(empty_dict)

# a = product(lista_kluczy[0], lista_kluczy[0], lista_list[0])
# for b in a:
#     print(b)

# products = [
#     {a, b, c}
#     for a in input_data["szerokość"]
#     for b in input_data["wysokość"]
#     for c in input_data["kolor"]
# ]

# print(products)
# print(input_data["szerokość"])

result = (
    dict(zip(input_data.keys(), values)) for values in product(*input_data.values())
)
for a in result:
    print(a)
"""
lista = [
    {'key1': 'set1key1', 'key2' :'set1key2', key3 : set1key3},
    {'key1': 'set2key1', 'key2' :'set2key2', key3 : set2key3},
]
"""
