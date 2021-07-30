import pywallet
import pandas
from tqdm import tqdm
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-doge", "--doge", action="store_true")
parser.add_argument("-lite", "--lite", action="store_true")
parser.add_argument("-zcash", "--zcash", action="store_true")
args = parser.parse_args()

# select chain
if args.doge:
    chain = "doge"
    network_doge = pywallet.Network('Dogecoin', 0x1e, 0x16, 0x9e, 'doge')
    pywallet.network = network_doge
elif args.zcash:
    chain = "zcash"
    network_zcash = pywallet.Network('Zcash', 0x1cb8, 0x1cbd, 0x80, 'zec')
    pywallet.network = network_zcash
elif args.lite:
    chain = "lite"
    network_lite = pywallet.Network('Litecoin', 48, 5, 176, 'ltc')
    pywallet.network = network_lite
else:
    raise ValueError("Please select --doge, --lite or --zcash")

# select files
wname = "%s.dat" % chain
wrdir = "./wallets"
csvf = "%s/%s.csv" % (wrdir, chain)

dbr_env = pywallet.create_env(wrdir)
# pywallet.create_new_wallet(dbr_env, wname, 1140300) # 180100
dbr = pywallet.open_wallet(dbr_env, wname, True)

# add private keys
df = pandas.read_csv(csvf)

for index, row in tqdm(df.iterrows()):
    addr = row["address"]
    publ = row["public key"]
    priv = row["private key"]

    pywallet.importprivkey(dbr, priv, "recovered: %s" % priv, True, True)

# pywallet.read_wallet(
#     pywallet.json_db, dbr_env, wname, True, True, "", None, True
# )

dbr.close()
