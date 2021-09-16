from controller.controller import Controller
from repository.blockchain_repository import BlockchainRepository


def start():
    BlockchainRepository()
    Controller()
    Bot()


if __name__ == '__main__':
    start()
