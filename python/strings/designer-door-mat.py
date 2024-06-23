# Enter your code here. Read input from STDIN. Print output to STDOUT
rows, cols = list(map(int, input().split()))

msg = "WELCOME"
sep = ".|."
sepCounter = 0
lineCounter = 0

lines = []

while lineCounter < rows / 2 - 1:
    lines.append((sep * (sepCounter + 1)).center(cols, "-"))
    sepCounter += 2
    lineCounter += 1

for i in range(0, lineCounter):
    print(lines[i])

print(msg.center(cols, "-"))

for i in range(0, lineCounter):
    print(lines[lineCounter - i - 1])
