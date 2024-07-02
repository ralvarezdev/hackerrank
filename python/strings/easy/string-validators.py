if __name__ == "__main__":
    s = input()
    isalnum = isalpha = isdigit = islower = isupper = False

    for c in s:
        if not isalnum:
            isalnum = c.isalnum()

        if not isalpha:
            isalpha = c.isalpha()

        if not isdigit:
            isdigit = c.isdigit()

        if not islower:
            islower = c.islower()

        if not isupper:
            isupper = c.isupper()

    validations = [isalnum, isalpha, isdigit, islower, isupper]

    for validation in validations:
        print(validation)
