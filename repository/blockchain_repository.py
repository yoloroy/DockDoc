from lib.singleton import singleton
from model.BOLs import BasicBOL
from model.block import Block


@singleton
class BlockchainRepository:
    def __init__(self):
        pass

    def add_block(self, block: Block):
        pass

    def add_values(self, *values: BasicBOL):
        pass

    def get_all(self):
        pass

    def invalidate_blocks(self):
        pass
