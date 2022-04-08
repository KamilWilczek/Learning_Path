input_data = {
    "szerokość": {"20cm", "16cm", "10cm"},
    "wysokość": {"30cm", "40cm"},
    "kolor": {"czarny", "biały", "zielony"},
}


def kartezjan(input_data):
    pusta_lista = []

    zbiory = [tuple(zbior) for zbior in input_data.values()]
    wynik = [[]]
    for zbior in zbiory:
        wynik = [x + [y] for x in wynik for y in zbior]
    for something in wynik:
        pusta_lista.append(something)

    print(pusta_lista)

    result = (dict(zip(input_data.keys(), values)) for values in pusta_lista)
    for a in result:
        return a
