# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

nCmds = int(input())
deque = deque()

for i in range(0, nCmds):
    cmd = input().split()

    if cmd[0] == "append":
        deque.append(int(cmd[1]))

    elif cmd[0] == "appendleft":
        deque.appendleft(int(cmd[1]))

    elif cmd[0] == "pop":
        deque.pop()

    elif cmd[0] == "popleft":
        deque.popleft()

print(" ".join([str(d) for d in deque]))