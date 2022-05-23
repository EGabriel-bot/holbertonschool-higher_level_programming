#!/usr/bin/python3
def matrix_divided(matrix, div):
    typeerr = "matrix must be a matrix (list of lists) of integers/floats"
    new = list(map(list, matrix))
    rowlength = len(new[0])
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(new)):
        if rowlength != len(new[i]):
            raise TypeError(
                "Each row of the matrix must have the same size")
        for j in range(len(new[i])):
            if type(new[i][j]) not in [int, float]:
                raise TypeError(typeerr)
            new[i][j] = new[i][j] / div
            new[i][j] = round(new[i][j], 2)

    return new
