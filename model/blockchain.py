import hashlib
import json
from time import time

from lib.iterator_funcs import flatten, sum_iterators
from model.block import Block


class Blockchain(object):
    def __init__(self, chain=None):
        self.current_values = []
        self.chain = chain if chain else []

        if not chain:
            self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = Block(
            len(self.chain) + 1,
            time(),
            self.current_values.copy(),
            proof,
            previous_hash or self.hash(self.chain[-1]),
        )

        # Reset the current list of documents
        self.current_values = []

        self.chain.append(block)
        return block

    def new_value(self, value):
        """
        Creates a new value to go into the next mined Block
        :param value: <Document> Value to put into chain
        :return: <int> The index of the Block that will hold this value
        """
        self.current_values.append(value)

        return self.last_block.index + 1

    def get_by_sent(self, sender):
        return filter(
            lambda bol: bol.sender == sender,
            flatten(map(lambda block: block.values, self.chain))
        )

    def get_by_received(self, receiver):
        return filter(
            lambda bol: bol.receiver == receiver,
            flatten(map(lambda block: block.values, self.chain))
        )

    def get_by_sender_receiver(self, sender, receiver):
        return filter(
            lambda bol: bol.sender == sender and bol.receiver == receiver,
            flatten(map(lambda block: block.values, self.chain))
        )

    def get_with_me(self, me):
        return sum_iterators(self.get_by_sent(me), self.get_by_received(me))

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block.as_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
