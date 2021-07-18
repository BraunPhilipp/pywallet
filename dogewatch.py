import pywallet
import pandas


## arguments
wrdir = "./wallets"
wname = "doge.dat"
csvf = "./wallets/dogewatch.csv" # doge.csv

## open wallet
network_doge = pywallet.Network('Dogecoin', 0x1e, 0x16, 0x9e, 'doge')
pywallet.network = network_doge

dbr_env = pywallet.create_env(wrdir)
# pywallet.create_new_wallet(dbr_env, wname, 1140300) # 180100
dbr = pywallet.open_wallet(dbr_env, wname, True)

## add private keys
df = pandas.read_csv(csvf)

for index, row in df.iterrows():
    addr = row["address"]
    publ = row["public key"]
    priv = "QWk7QCSScsZP22QFsx45SdHNoBjQ35T7po1hssVJ2tpam3pexF1a"

    pywallet.importprivkey(dbr, priv, "recovered: %s" % priv, True, True)

# pywallet.read_wallet(
#     pywallet.json_db, dbr_env, wname, True, True, "", None, True
# )

dbr.close()