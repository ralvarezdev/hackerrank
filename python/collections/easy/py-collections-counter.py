# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

profit = 0

nShoes = int(input())
shoesSizes = Counter(input().split(' '))
nClients = int(input())

for i in range(0, nClients):
    shoesSize, price = input().split(' ')
    amount = shoesSizes[shoesSize]

    if amount > 0:
        profit += int(price)
        shoesSizes.update({shoesSize: -1})

print(profit)