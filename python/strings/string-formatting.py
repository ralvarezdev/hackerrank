def print_formatted(number):
    maxSize = len(str(bin(number))[2:])

    for i in range(1, number + 1):
        conv = [str(i), str(oct(i))[2:], str(hex(i))[2:].upper(), str(bin(i))[2:]]

        print(" ".join([c.rjust(maxSize) for c in conv]))


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
