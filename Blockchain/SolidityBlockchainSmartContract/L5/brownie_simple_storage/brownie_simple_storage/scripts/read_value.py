from brownie import SimpleStorage, accounts, config


def read_contract():
    print("SimpleStorage", SimpleStorage)
    print("SimpleStorage[0]", SimpleStorage[0])
    # 0 for first one deployments, -1 for the most fresh
    simple_storage = SimpleStorage[-1]
    # go take the index that's one less than the length
    # ABI
    simple_storage.retrieve()
    # Address


def main():
    read_contract()
