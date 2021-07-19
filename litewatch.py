import pandas
import time
from datetime import datetime
import requests
import json

# arguments
csvf = "./wallets/litewatch.csv"
xpub = "Ltub2Yb43FU88n77HhRjTPWMtpgY1LurEAcyVwCKfbjpT39VQheywiLPtYwjzWopdgMKdBug5RKKxHcQD11qYR5FyY1NBfThR3hLUa4MAtCGiWN"

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
    endpoint = f"https://api.blockchair.com/litecoin/addresses/balances?addresses={addresses_batch}"
    data = json.loads(requests.get(endpoint).text)["data"]
    print(data)
    if data is not None and not isinstance(data, list):
        for k, v in data.items():
            balance += float(v) / (10**8)
    time.sleep(0.1)

print(balance)

# 277.3160058599999 LTC (33235.43 USD)