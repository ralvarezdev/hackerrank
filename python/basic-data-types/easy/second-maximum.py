if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    first = None
    second = None

    for i in arr:
        if first is None or i > first:
            second = first
            first = i

        elif i < first:
            if second is None or i > second:
                second = i

    print(second)
