# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

nWords = int(input())
words = OrderedDict()

for i in range(0, nWords):
    word = input()

    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = 1

wordsCounter = []
for key in words:
    wordsCounter.append(words[key])

print(len(words))
print(" ".join(map(str, wordsCounter)))