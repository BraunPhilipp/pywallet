import pandas
from bipwallet import wallet

xpub_addr = "dgub8roKwYEpHT6MX6CCofpkhF9UZtHvMfKXLwcFqY34MsasoomwDo7mTi6CLLJFbnjrxuhvz5gZFaAJcSPw2ZaRa8c6qfWhQQ2MShAAh4B9d36"
key_data = []

seed = wallet.generate_mnemonic()
w = wallet.create_wallet(network="DOGE", seed=seed, children=1000)
children = w["children"]

for child in children:
    key_data.append(
        [child["address"], child["public_key"], child["private_key"]] # fake key from random seed
    )
# print(key_data)

df = pandas.DataFrame(key_data)
header = ["address", "public key", "private key"]
df.to_csv("data/dogewatch.csv", header=header)