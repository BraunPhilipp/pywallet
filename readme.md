## PulseChain Tracking Tool

Scripts in this repo can be used to import private keys and monitor public keys for dogecoin and litecoin.

### Instructions

1. Copy current `wallet.dat` into `wallets` directory from your `%appdata%` directory (Windows)
2. Rename `wallet.dat` to `doge.dat` or `lite.dat`
3. Derive public and private keys using https://iancoleman.io/bip39/#english
4. Copy csv file into the `wallets` directory as `doge.csv` or `lite.csv`
5. Run the wallet injection script
6. Copy the modified `.dat` file and rename to `wallet.dat`
7. Run you wallet client

````
docker build -t pywallet .
docker run -it --rm -v C:/Users/35898/OneDrive/Desktop/pywallet:/home -p 8050:8050 pywallet

python doge.py &> doge.log
python lite.py &> lite.log
python3 dogewatch.py &> dogewatch.log
python3 litewatch.py &> litewatch.log
````

## References

1. https://iancoleman.io/bip39/#english
2. https://github.com/cryptocoinjs/coininfo/tree/master/lib/coins
3. https://github.com/bitcoin/bips/blob/8659829de1d599ab6f36810ac6a14394ca1e16f5/bip-0032.mediawiki
