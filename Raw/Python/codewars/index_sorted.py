input = [4, 7, 9, 11, 11, 13, 23]
n = 12


def index_sorted(input, n):
    D = dict()
    for i, item in enumerate(input):
        if item not in D:
            D[item] = [i]
    try:
        return D[n]
    except:
        return None
