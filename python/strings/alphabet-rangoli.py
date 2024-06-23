def print_rangoli(size):
    maxAsciiInt = size + ord("a") - 1

    msg = []
    lineCounter = 0

    while lineCounter < size:
        tempMsg = []

        for i in range(0, lineCounter):
            tempMsg.append(chr(maxAsciiInt - i))

        tempMsg.append(chr(maxAsciiInt - lineCounter))

        for i in range(0, lineCounter):
            tempMsg.append(chr(maxAsciiInt - lineCounter + i + 1))

        msg.append("-".join(tempMsg).center(4 * size - 3, "-"))
        lineCounter += 1

    for i in range(0, size - 1):
        msg.append(msg[size - 2 - i])

    print("\n".join(msg))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
