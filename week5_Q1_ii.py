def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def add_matrices(matrix1, matrix2):
    result = [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))]
        for i in range(len(matrix1))
    ]
    return result

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = add_matrices(matrix1, matrix2)
print("Result of addition:")
print_matrix(result_matrix)
