#Zero matrix

#Time complexity O(n^3)

def fill_zeros(matrix, row, col):
    for i in range(len(matrix)):
        matrix[i][row] = 0

    for j in range(len(matrix[0])):
        matrix[col][j] = 0

    return matrix


def zero_matrix_solution(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix = fill_zeros(matrix, i, j)
                return matrix

    return matrix
