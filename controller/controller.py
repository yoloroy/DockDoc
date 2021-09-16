import random

from lib.singleton import singleton
from model.blockchain import Blockchain


@singleton
class Controller:
    def __init__(self, load_chain=False):
        self.chain = Blockchain([] if load_chain else [])  # TODO: add loading
        self.not_approved_docs = {-1: None}

    def add_document(self, document):
        self.not_approved_docs[self.max_index + 1] = document
        return self.max_index

    def approve_document(self, document_id):
        self.chain.new_value(self.not_approved_docs[document_id])
        self.chain.new_block(random.randint(-8000, 8000))  # TODO: move to parallel thread

    def disapprove_document(self, document_id):
        del self.not_approved_docs[document_id]

    def get_for(self, sender=None, receiver=None, anyone=None):
        assert sender or receiver or anyone

        if sender and receiver:
            return self.get_for_sender_and_receiver(sender, receiver)
        if sender:
            return self.get_for_sender(sender)
        if receiver:
            return self.get_for_receiver(receiver)
        if anyone:
            return self.get_with_me(anyone)

    def get_for_sender(self, sender):
        return list(self.chain.get_by_sent(sender))

    def get_for_receiver(self, receiver):
        return list(self.chain.get_by_received(receiver))

    def get_with_me(self, me):
        return list(self.chain.get_with_me(me))

    def get_for_sender_and_receiver(self, sender, receiver):
        return list(self.chain.get_by_sender_receiver(sender, receiver))

    @property
    def max_index(self):
        if not self.not_approved_docs:
            return 0
        return max(self.not_approved_docs)
