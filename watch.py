import pandas
import time
from datetime import datetime
import requests
import json
import argparse


# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-doge", "--doge", action="store_true")
parser.add_argument("-lite", "--lite", action="store_true")
parser.add_argument("-zcash", "--zcash", action="store_true")
args = parser.parse_args()

# select chain
if args.doge:
    chain = "dogecoin"
    csvf = "./wallets/doge-watch.csv"
elif args.doge:
    chain = "litecoin"
    csvf = "./wallets/lite-watch.csv"
elif args.zcash:
    chain = "zcash"
    csvf = "./wallets/zcash-watch.csv"
else:
    raise ValueError("Please select --doge, --lite or --zcash")


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

print(f">> {balance} {chain}")
