import pandas
import time
from datetime import datetime
import requests
import json


# arguments
csvf = "./wallets/dogewatch.csv"
csvf = "./wallets/litewatch.csv"


chain = "dogecoin" # litecoin



# get addresses
df = pandas.read_csv(csvf)
balance = 0

addresses = []
for index, row in df.iterrows():
    address = row["address"]
    public_key = row["public key"]
    addresses.append(address)

balance = 0
for idx in range(0, len(addresses), 200):
    addresses_batch = addresses[idx:idx+200]
    addresses_batch = ",".join(addresses_batch)
    endpoint = f"https://api.blockchair.com/{chain}/addresses/balances?addresses={addresses_batch}"
    data = json.loads(requests.get(endpoint).text)["data"]
    print(data)
    if data is not None and not isinstance(data, list):
        for k, v in data.items():
            balance += float(v) / (10**8)
    time.sleep(0.1)

print(balance)

# 1499430.6675273506 DOGE (238680.41 USD)
