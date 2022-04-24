from brownie import accounts, config, SimpleStorage, network

# import os


def deploy_simple_storage():
    # methods for accessing account
    # account = accounts[0]
    # account = accounts.load("memask-test-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    account = get_account()
    # print("account", account)

    simple_storage = SimpleStorage.deploy({"from": account})
    # brownie is smart enought to figure out which one to perform
    # Transact
    # Call
    print("simple_storage", simple_storage)
    stored_value = simple_storage.retrieve()
    print("stored_value", stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print("updated_stored_value", updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
