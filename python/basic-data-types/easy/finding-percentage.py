from functools import reduce

if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    query = student_marks[query_name]
    scoresLen = len(query)

    result = reduce(lambda a, b: a + b, query)
    print("{:.2f}".format(result / scoresLen))
