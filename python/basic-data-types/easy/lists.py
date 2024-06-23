if __name__ == "__main__":
    N = int(input())
    numbers = []

    for i in range(0, N):
        op = input().split()
        opName = op[0]

        if opName == "insert":
            numbers.insert(int(op[1]), int(op[2]))

        elif opName == "print":
            print(numbers)

        elif opName == "remove":
            numbers.remove(int(op[1]))

        elif opName == "append":
            numbers.append(int(op[1]))

        elif opName == "sort":
            numbers.sort()

        elif opName == "pop":
            numbers.pop()

        elif opName == "reverse":
            numbers.reverse()
