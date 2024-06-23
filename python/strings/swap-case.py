def swap_case(s):
    swapStr = ""

    for i in s:
        if not i.isalpha():
            swapStr += i
            continue

        swapStr += i.upper() if i.islower() else i.lower()

    return swapStr


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
