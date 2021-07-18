import pandas
import time
from datetime import datetime
import requests
import json


# arguments
csvf = "./wallets/litewatch.csv"
xpub = "dgub8roKwYEpHT6MX6CCofpkhF9UZtHvMfKXLwcFqY34MsasoomwDo7mTi6CLLJFbnjrxuhvz5gZFaAJcSPw2ZaRa8c6qfWhQQ2MShAAh4B9d36"

# https://iancoleman.io/bip39/#english
# https://blockchair.com/bitcoin/xpub/xpub6DXRxywCQ9ampUyumwiFiRQ1MTf5oKLipT3YQHyh88co6Eh2epEZvuX7eFGufdEzGw7rAoxRqBFNpTXKAmFYbZe4QeudCMjKtfwYrkuDHod

# get addresses
df = pandas.read_csv(csvf)
balance = 0

addresses = []
for index, row in df.iterrows():
    address = row["address"]
    public_key = row["public key"]
    addresses.append(address)

balance = 0
for idx in range(0, len(addresses), 100):
    addresses_batch = addresses[idx:idx+100]
    addresses_batch = ",".join(addresses_batch)
    endpoint = f"https://api.blockchair.com/litecoin/addresses/balances?addresses={addresses_batch}"
    data = json.loads(requests.get(endpoint).text)["data"]
    print(data)
    if data is not None and not isinstance(data, list):
        for k, v in data.items():
            balance += float(v) / (10**8)
    time.sleep(0.1)

print(balance)

# 140845.99053285999 DOGE (24707.59 USD)
# 97.71593967999999 LTC (11436.8 USD)