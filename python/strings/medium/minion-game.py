import re


def minion_game(string):
    consonantsPlayer = "Stuart"
    consonantsIndexes = []
    consonantsCounter = 0

    vowelsPlayer = "Kevin"
    vowelsIndexes = []
    vowelsCounter = 0

    index = 0

    for c in string:
        if re.match(r'[aeiouAEIOU]', c):
            vowelsIndexes.append(index)

        elif c.isalpha():
            consonantsIndexes.append(index)

        index += 1

    for i in consonantsIndexes:
        consonantsCounter += index - i

    for i in vowelsIndexes:
        vowelsCounter += index - i

    if consonantsCounter == vowelsCounter:
        print("Draw")

    elif consonantsCounter > vowelsCounter:
        print(f'{consonantsPlayer} {consonantsCounter}')

    else:
        print(f'{vowelsPlayer} {vowelsCounter}')


if __name__ == '__main__':
    s = input()
    minion_game(s)