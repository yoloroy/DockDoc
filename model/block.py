from dataclasses import dataclass
from typing import List

from model.BOLs import BasicBOL


@dataclass(frozen=True)
class Block:
    index: int
    timestamp: float
    values: List[BasicBOL]
    proof: int
    previous_hash: str

    def as_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "values": list(map(lambda bol: bol.as_dict(), self.values)),
            "proof": self.proof,
            "previous_hash": self.previous_hash,
        }
