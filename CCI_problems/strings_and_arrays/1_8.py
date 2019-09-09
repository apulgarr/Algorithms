#Zero matrix

#Time complexity O(n^2)

def fill_zeros(matrix, row, col):
    for pos_i in range(len(matrix)):
        matrix[pos_i][col] = 0

    for pos_j in range(len(matrix[0])):
        matrix[row][pos_j] = 0

    return matrix


def find_zeros(matrix):
    arr_pos = []

    for pos_i in range(len(matrix)):
        for pos_j in range(len(matrix[0])):
            if matrix[pos_i][pos_j] == 0:
                arr_pos.append((pos_i,pos_j))


    return arr_pos


def solution(matrix):
    if len(matrix) == 0:
        return 0

    arr_pos = find_zeros(matrix)

    for value in arr_pos:
        matrix = fill_zeros(matrix, value[0], value[1])

    return matrix
