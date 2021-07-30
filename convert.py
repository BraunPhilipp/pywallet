import pandas

df = pandas.read_csv("./wallets/zcash.csv")

for index, row in df.iterrows():
    priv = row["private key"]
    print(priv)
