import numpy

dimension = int(input())
matrix = []

for _ in range(0, dimension):
    matrix.append(list(map(float, input().split())))

print(round(numpy.linalg.det(matrix), 2))
