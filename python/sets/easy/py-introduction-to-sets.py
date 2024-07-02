from functools import reduce


def average(array):
    arraySet = set(array)
    average = reduce(lambda a, b: a + b, arraySet) / len(arraySet)

    return "{:0.3f}".format(average)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)