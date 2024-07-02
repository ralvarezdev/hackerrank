# Enter your code here. Read input from STDIN. Print output to STDOUT4
from collections import defaultdict

groupASize, groupBSize = list(map(int, input().split()))

groupA = defaultdict(list)
for i in range(1, groupASize + 1):
    groupA[input()].append(i)

groupB = list()
for _ in range(0, groupBSize):
    groupB.append(input())

for element in groupB:
    results = groupA[element]

    print(-1 if len(results) == 0 else " ".join(map(str, results)))