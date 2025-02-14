import requests

def get_transaction_count_from_etherscan(address, api_key):
    url = (
        f"https://api.etherscan.io/api"
        f"?module=account"
        f"&action=txlist"
        f"&address={address}"
        f"&startblock=0"
        f"&endblock=99999999"
        f"&page=1"
        f"&offset=10000"
        f"&sort=asc"
        f"&apikey={api_key}"
    )
    response = requests.get(url).json()
    if response['status'] == '1':
        return len(response['result'])  # Number of transactions
    else:
        print("Error:", response['message'])
        return None

# Replace with your Etherscan API Key
etherscan_api_key = "SDI5QEC2UAY1CX4C1VPXC4WE9HIMH2SF1C"

file = open("erc20.txt")
# test = get_transaction_count_from_etherscan(address="0x88093840aad42d2621e1a452bf5d7076ff804d61" , api_key=etherscan_api_key)
for line in file.readlines():
    line = line.strip()
    address = "0x" + line.split("0x")[-1]
    transaction_count = get_transaction_count_from_etherscan(address, etherscan_api_key)
    if transaction_count and transaction_count > 50:
       print(f"python3 -m invconplus.main --address {address}")
