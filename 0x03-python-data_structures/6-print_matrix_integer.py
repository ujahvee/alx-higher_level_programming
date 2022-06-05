#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for p in range(len(matrix[i])):
            if p != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][p]), end='')
        print()
