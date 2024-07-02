# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

nTests = int(input())
nBlocks = []
blocksList = []

for i in range(0, nTests):
    nBlocks.append(int(input()))
    currBlockList = deque(map(int, input().split()))
    blocksList.append(currBlockList)

for b in blocksList:
    top = b.popleft() if b[0] >= b[-1] else b.pop()

    while True:
        originalSize = len(b)
        if originalSize == 0:
            break

        if b[-1] <= b[0] <= top:
            top = b.popleft()

        elif b[0] <= b[-1] <= b[-1] <= top:
            top = b.pop()

        if originalSize == len(b):
            break

    print("Yes" if len(b) == 0 else "No")