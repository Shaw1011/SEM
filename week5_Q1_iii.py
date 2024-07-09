def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def multiply_matrices(matrix1, matrix2):
    size = len(matrix1)
    result = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

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

result_matrix = multiply_matrices(matrix1, matrix2)
print("Result of multiplication:")
print_matrix(result_matrix)
