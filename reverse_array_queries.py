# Reverse Array Queries.
"""
For a given array of integers, perform operations on the array. Return the resulting array after all operations have been applied in the order given. Each operation contains two indices. Reverse the subarray between those zero-based indices.
"""

#
# Complete the 'performOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY operations
#


def performOperations(arr, operations):
    for i in operations:
        arr[i[0]:i[1]+1] = reversed(arr[i[0]:i[1]+1])
    return arr


if __name__ == '__main__':
    arr = [5, 3, 2, 1, 3]
    operations = [[0, 1], [1, 3]]
    print(performOperations(arr, operations))
