def count_substring(string, sub_string):
    tempString = string
    counter = 0

    while True:
        idx = tempString.find(sub_string)

        if idx == -1:
            break

        tempString = tempString[idx + 1 :]
        counter += 1

    return counter


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
