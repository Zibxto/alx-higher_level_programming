#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        result = []
        for x in matrix:
            row_result = []
            for y in x:
                row_result.append(y ** 2)
            result.append(row_result)
        return result
    else:
        return None
