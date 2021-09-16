def print_list_of_BOLs(bols, header=""):
    if header:
        print(header)
    print(
        "\n".join(map(lambda x: str(x), bols)),
        end='\n\n'
    )


def to_currency_tuple(postString):
    number, currency = postString.split()
    return int(number), currency
