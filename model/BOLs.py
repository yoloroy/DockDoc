from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class BasicBOL:
    sender: str
    receiver: str
    goods_type: str
    goods_amount: str
    goods_value: Tuple[int, str]  # pair of (cents(or other minimal value): int, currency name (as USD, EUR...): str)
    place_of_start: str
    place_of_receive: str
    doc_creation_time: int  # seconds from start of epoch

    def as_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "goods_type": self.goods_type,
            "goods_amount": self.goods_amount,
            "goods_value": self.goods_value,
            "place_of_start": self.place_of_start,
            "place_of_receive": self.place_of_receive,
            "doc_creation_time": self.doc_creation_time
        }
