import json
import requests    

rpc_user="zecwallet"
rpc_password="cd3u0td7d5t"

# curl --user zecwallet --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressbalance", "params": [{"addresses": ["tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ"]}] }' -H 'content-type: text/plain;' http://127.0.0.1:18232/


url = "http://127.0.0.1:18232/"
payload = json.dumps({"method": "getaddressbalance", "params": [{"addresses": ["t1KLUV7nQE7htr8q9hjxbtB5zhzYZYCEPbK"]}]})
headers = {'content-type': "application/json", 'cache-control': "no-cache"}

response = requests.request("POST", url, data=payload, headers=headers, auth=(rpc_user, rpc_password))
response = json.loads(response.text)

print(response)


# rpcuser=zecwallet
# rpcpassword=cd3u0td7d5t
# rpcallowip=127.0.0.1
# rpcbind=127.0.0.1
# rpcport=18232