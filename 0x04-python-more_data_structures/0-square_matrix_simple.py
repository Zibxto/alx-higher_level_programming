#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        result = []
        for x in matrix:
            for y in x:
                result.append(y ** 2)
            result_list = list(result)
        return result_list
    else:
        return None
