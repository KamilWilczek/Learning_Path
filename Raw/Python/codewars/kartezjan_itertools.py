from itertools import product

input_data = {
    "szerokość": {"20cm", "16cm", "10cm"},
    "wysokość": {"30cm", "40cm"},
    "kolor": {"czarny", "biały", "zielony"},
}

result = (
    dict(zip(input_data.keys(), values)) for values in product(*input_data.values())
)
for a in result:
    print(a)

# def my_product(inp):
#     return (dict(zip(inp.keys(), values)) for values in product(*inp.values())


def product(*args, repeat=1):
    zbiory = [tuple(zbior) for zbior in input_data.values()]
    wynik = [[]]
    for zbior in zbiory:
        wynik = [x + [y] for x in wynik for y in zbior]
    for something in wynik:
        yield tuple(something)
