if __name__ == "__main__":
    students = {}
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score not in scores:
            scores.append(score)

        if score not in students:
            students[score] = [name]
        else:
            students[score].append(name)

    scores.sort()
    secondLowest = scores[1]

    secondLowestStudents = students[secondLowest]
    secondLowestStudents.sort()

    for student in secondLowestStudents:
        print(student)
