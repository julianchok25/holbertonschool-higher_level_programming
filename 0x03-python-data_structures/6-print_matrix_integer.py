#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix is None):
        print()
    else:
        for i in range(len(matrix)):
            print("{}".format(matrix[i]))
