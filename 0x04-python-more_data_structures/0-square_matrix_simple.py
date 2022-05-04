#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
      new = list(map(list, matrix))
      for i in range(len(new)):
          for j in range(len(new)):
              new[i][j] = new[i][j] * new[i][j]

      return new
