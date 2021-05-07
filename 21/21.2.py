def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


matrix = [[1, 2], [3, 4]]
matrix = transpose(matrix)
for line in matrix:
    print(*line)

