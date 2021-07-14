## Run

Before running make sure to copy your current `wallet.dat` backup into the `data` directory and rename to `doge.dat` or `lite.dat`. Copy the the csv file with the public and private keys into the same directory. The script will add the keys in the csv file to
the wallet. After adding all the keys you will need to rename and copy the augmented file back to your `%appdata%` directory (windows). Running the wallet will take approx. 2 hours to rescan. All balances should show up without issues.

````
docker build -t pywallet .
docker run -it --rm -v C:/Users/35898/OneDrive/Desktop/pywallet:/home -p 8050:8050 pywallet

python doge.py &> doge.log
python lite.py &> lite.log
````

## Network Identifiers

```
## doge
# bech32: 'doge',
# bip44: 3,
# private: 0x9e,
# public: 0x1e,
# scripthash: 0x16

## btc
# bech32: 'bc',
# bip44: 0,
# private: 0x80,
# public: 0x00,
# scripthash: 0x05

## ltc
# bech32: 'ltc',
# bip44: 1,
# private: 0xef,
# public: 0x6f,
# scripthash: 0x3a,
# scripthash2: 0xc4
```

## References

1. https://iancoleman.io/bip39/#english
2. https://github.com/cryptocoinjs/coininfo/tree/master/lib/coins


## Test wallet

## Doge & Litecoin

### Mnemonic
parent love together arm voice grid chat release riot patch code sing barrel depart dilemma

### BIP 39 Seed
bc7e468adce645083ea37d5b23034d37efc50ec35ac059ce713959d2838210a14e1c1ff0030170aad87af55d4b045d3ee04cb23c7cb8c8fa53f912c7ecddaa6f

### BIP 32 Root (Doge)
dgpv51eADS3spNJh8PH91ZyKFDWnZ5hxiiaf5AJiiQKRyA1ASwRKgAdJP7sMK8sS7yyCWwukQq64yBoSwW9VPhp4dRvmDtyAAKUS1pRvhkZHiv9

### BIP 32 Root (Litecoin)
Ltpv71G8qDifUiNesVe36PHwiG3UQaZUAoRLN4zMTJgztNKYaoaHUN72AQaUdnobvYXuXtoaAYgRaxV8GC9T1Wm4Yv3L2Hz7KuPYpakeD6k18GH

### Test (Doge)
m/44'/3'/0'/0/0,DHGu4JPvsFgayTeSAsxN6Vm8Tovpk4PJwe,02b621c030d526575af1a9c1a138fa0dd0cca29b3ebd2b02836daf1ba07e65d58f,QWk7QCSScsZP22QFsx45SdHNoBjQ35T7po1hssVJ2tpam3pexF1a
m/44'/3'/0'/0/12,DQM15iB6xgGqJ4sYCV367CTXyeGUDoyjZx,030233654daa3a701434078ef08e3071fb370b055f1deb6a389f6114d755655047,QRk2vZFpD1huTJ2wAEKv6WkWBTVuMWc97UzdKxvNHS87yA82UrtJ

### Test (Litecoin)

m/44'/2'/0'/0/0,LdxUqcVNXgYCQaFtQbQ7SoFJBKeLnB7xtn,03ff7fcd9f445bee9ade2ecf2e2b40af7e213ef2a07e3e619b831c8cb820d55c12,TAe86xj8iDqn3M3f6PtD4tmCCQiosUiskfZqR9GtFMP1GseL9MRv
m/44'/2'/0'/0/17,LiShhj8UYamM4q9e7bgGHgFYfVVpRE5yoF,02cfeb403b6b88677efcb04766a6e5409031a8374376a2de3f5cc4e08fb3a085d0,T8HBpUgJ5VnndxSfhqRQzahGFjEw2UmZxkWhgMpsEwP1RmDmGQSc
