import json
import requests    

rpc_user="zecwallet"
rpc_password="cd3u0td7d5t"
url = "http://127.0.0.1:18232/"

# curl --user zecwallet --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressbalance", "params": [{"addresses": ["tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ"]}] }' -H 'content-type: text/plain;' http://127.0.0.1:18232/


zecf = open("./wallets/zcash-watch.csv", "r")
pubs = zecf.readlines()
pubs = [pub.split(",")[1].strip().replace("\n", "") for pub in pubs]

total = 0

for idx in range(0, len(pubs), 200):
    pubsBatch = pubs[idx:idx+200]

    # print(pubsBatch)

    payload = json.dumps({"method": "getaddressbalance", "params": [{"addresses": pubsBatch}]})
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}

    response = requests.request("POST", url, data=payload, headers=headers, auth=(rpc_user, rpc_password))
    response = json.loads(response.text)

    if response["result"] is not None:
        print(response["result"])
        total += float(response["result"]["received"]) / (10**8)

    # print(response)

print(total)

# rpcuser=zecwallet
# rpcpassword=cd3u0td7d5t
# rpcallowip=127.0.0.1
# rpcbind=127.0.0.1
# rpcport=18232