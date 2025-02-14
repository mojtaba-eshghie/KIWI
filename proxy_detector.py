import requests


def ping_etherscan(address:str):
    data = requests.post(f"https://api.etherscan.io/api?module=contract&action=verifyproxycontract&address={address}&apikey=SDI5QEC2UAY1CX4C1VPXC4WE9HIMH2SF1C")
    print(data.text)



file = open("dataset.txt")


for line in file.readlines():
    ping_etherscan(line.strip())
    break


