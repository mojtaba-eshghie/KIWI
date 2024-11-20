
file = open("dataset.txt")
for line in file.readlines():
    line = line.strip()
    line = line.split("0x")
    print(line)
    break
    set.add(line)


for contract in set:
    print(f"python3 -m invconplus.main --address {contract}")
