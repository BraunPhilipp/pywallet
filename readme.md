## Wallet tracking & import tool

Scripts in this repo can be used to import private keys and monitor public keys for dogecoin, litecoin and zcash. The tool
was primarily built to monitor addresses during the pulsechain sacrifice phase. 

### Instructions

**Wallet import**

1. Copy current `wallet.dat` from your `%appdata%` directory into the `wallets` directory (Windows)
2. Rename `wallet.dat` to `doge.dat`, `lite.dat` or `zcash.dat` depending on the chain you choose
3. Derive public and private keys using https://iancoleman.io/bip39/#english
4. Copy csv file into the `wallets` directory as `doge.csv`, `lite.csv` or `zcash.csv`
5. Run the wallet injection script
6. Copy the modified `.dat` file and rename to `wallet.dat`
7. Run you wallet client and resync

**Wallet tracking**

1. Generate a csv file using  https://iancoleman.io/bip39/#english from xpub
2. Copy and rename the csv file to `doge-watch.csv`, `lite-watch.csv` or `zcash-watch.csv` inside your `wallets` directory
3. Execute your `watch.py --zcash` or your respective chain

**Note**

Wallet tracking might fail for too many API calls due to rate limiting by BlockChair. ZCash Qt supports address book import from a modified CSV file. LiteCoin is upgraded to a Bitcoin Core client that supports address imports via RPC calls. For DogeCoin I was not able to find any usable RPC call.

````
docker build -t pywallet .
docker run -it --rm -v C:/Users/35898/OneDrive/Desktop/pywallet:/home -p 8050:8050 pywallet

python wallet.py --doge
python3 watch.py --doge
````

### Addresses

```
dogecoin,secp256k1,dgub8roKwYEpHT6MX6CCofpkhF9UZtHvMfKXLwcFqY34MsasoomwDo7mTi6CLLJFbnjrxuhvz5gZFaAJcSPw2ZaRa8c6qfWhQQ2MShAAh4B9d36
litecoin,secp256k1,Ltub2Yb43FU88n77HhRjTPWMtpgY1LurEAcyVwCKfbjpT39VQheywiLPtYwjzWopdgMKdBug5RKKxHcQD11qYR5FyY1NBfThR3hLUa4MAtCGiWN
zcash,secp256k1,xpub6Cjo32WEp9mQLYCHXuCKUtfMspa6gaxr13nwP98G1HbNGwTJmSbrNGxu18cyJnjrCFMMGzeVGYUTFhaD3A248XDQoEpcz3pEdAdxhhgSn5i
```

## References

1. https://iancoleman.io/bip39/#english
2. https://github.com/cryptocoinjs/coininfo/tree/master/lib/coins
3. https://github.com/bitcoin/bips/blob/8659829de1d599ab6f36810ac6a14394ca1e16f5/bip-0032.mediawiki
4. https://github.com/jackjack-jj/pywallet
