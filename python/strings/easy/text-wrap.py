def wrap(string, max_width):
    wrappedText = []

    while max_width < len(string):
        wrappedText.append(string[:max_width])
        string = string[max_width:]

    if len(string) > 0:
        wrappedText.append(string)

    return "\n".join(wrappedText)


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
