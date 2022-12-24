__version__ = '0.1'

from random import randint
from copy import deepcopy


def matrix_full(matrix) -> list:
    num = 0
    colum = 0
    row = 0
    matrix_copy = deepcopy(matrix)

    for colum in range(len(matrix)):
        for row in range(len(matrix[colum])):
            num = randint(10, 99)
            matrix[colum][row] = str(num) if (num % 2 == 0) else '00'
            matrix_copy[colum] = matrix[colum].copy()

    matrix = matrix_copy.copy()
    del matrix_copy

    return matrix


def matrix_generator(row=5, colum=5) -> list:
    matrix = [[[]]*row]*colum

    return matrix


def display_matrix(matrix_method, row=None, colum=None) -> print:

    def display(matrix):
        for colum in range(len(matrix)):
            print()
            for row in range(len(matrix[colum])):
                print(matrix[colum][row], end='|')

    if (row and colum) is None:
        out_matrix = matrix_method(matrix_generator())
    elif (row or colum) is None:
        return 'Enter all argument\'s!'
    else:
        out_matrix = matrix_method(matrix_generator(row=row, colum=colum))

    return display(out_matrix)


def main():
    display_matrix(matrix_full)


main()
