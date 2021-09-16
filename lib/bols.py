def next_field(current):
    fields = [
        "start_state",
        "sender",
        "receiver",
        "goods_type",
        "goods_amount",
        "goods_value",
        "place_of_start",
        "place_of_receive",
        "final"
    ]

    return fields[min(fields.index(current) + 1, len(fields) - 1)]