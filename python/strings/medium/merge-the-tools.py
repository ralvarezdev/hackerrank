def merge_the_tools(string, k):
    split = []
    formatted = []

    for i in range(0, len(string) // k):
        split.append(string[i * k:(i + 1) * k])

    for word in split:
        encountered = dict()
        counter = 0

        for c in word:
            if c not in encountered:
                encountered[c] = True
                counter += 1

            else:
                word = word[:counter] + word[counter + 1:]

        formatted.append(word)

    for word in formatted:
        print(word)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)