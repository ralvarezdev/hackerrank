# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
from functools import reduce

nStudents = int(input())
colsName = input().split()
Student = namedtuple('Student', ','.join(colsName))
students = []

for i in range(0, nStudents):
    students.append(Student(*input().split()))

marks = list(map(int, [s.MARKS for s in students]))
results = reduce(lambda a, b: a + b, marks) / len(students)

print(results)