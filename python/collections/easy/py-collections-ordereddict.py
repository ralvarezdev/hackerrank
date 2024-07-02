# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

items = OrderedDict()
nItems = int(input())

for i in range(0, nItems):
    *itemName, netPrice = input().split()
    itemName = " ".join(itemName)

    if itemName in items:
        items[itemName] = items[itemName] + int(netPrice)
    else:
        items[itemName] = int(netPrice)

for key in items.keys():
    print(f"{key} {items[key]}")

