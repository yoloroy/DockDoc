def print_list_of_BOLs(bols, header=""):
    if header:
        print(header)
    print(
        "\n".join(map(lambda x: str(x), bols)),
        end='\n\n'
    )
