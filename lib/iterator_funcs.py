def flatten(t):
    return (item for sublist in t for item in sublist)


def sum_iterators(a, b):
    return flatten((a, b))
