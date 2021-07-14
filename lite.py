import pywallet
import pandas


## arguments
wrdir = "./data"
wname = "lite.dat"
csvf = "./data/lite.csv"

# base58Prefixes[PUBKEY_ADDRESS] = std::vector<unsigned char>(1,48);
# base58Prefixes[SCRIPT_ADDRESS] = std::vector<unsigned char>(1,5);
# base58Prefixes[SCRIPT_ADDRESS2] = std::vector<unsigned char>(1,50);
# base58Prefixes[SECRET_KEY] =     std::vector<unsigned char>(1,176);
# base58Prefixes[EXT_PUBLIC_KEY] = {0x04, 0x88, 0xB2, 0x1E};
# base58Prefixes[EXT_SECRET_KEY] = {0x04, 0x88, 0xAD, 0xE4};

## open wallet
network_lite = pywallet.Network('Litecoin', 48, 5, 176, 'ltc')
pywallet.network = network_lite

dbr_env = pywallet.create_env(wrdir)
# pywallet.create_new_wallet(dbr_env, wname, 1140300) # 180100
dbr = pywallet.open_wallet(dbr_env, wname, True)

## add private keys
df = pandas.read_csv(csvf)

for index, row in df.iterrows():
    addr = row["address"]
    publ = row["public key"]
    priv = row["private key"]

    pywallet.importprivkey(dbr, priv, "recovered: %s" % priv, True, True)

# pywallet.read_wallet(
#     pywallet.json_db, dbr_env, wname, True, True, "", None, True
# )

dbr.close()
