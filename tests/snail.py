def snail(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    row_begin = 0
    row_end = rows - 1
    col_begin = 0
    col_end = cols - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end + 1):
            result.append(matrix[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end + 1):
            result.append(matrix[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                result.append(matrix[row_end][i])
            row_end -= 1

        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                result.append(matrix[i][col_begin])
            col_begin += 1

    return result




# In this implementation, we use four variables to keep track of the current row and column ranges that we need to traverse. 
# We start by traversing the first row from left to right and then increment the row_begin variable to move to the next row. 
# We then traverse the last column from top to bottom and decrement the col_end variable to move to the previous column. 
# We continue this process until we have covered all elements of the matrix. Finally, we return the result list.








def test_snail_solution():
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert snail(arr) == expected

    arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
    assert snail(arr) == expected

    arr = [
        [1, 2, 3, 4, 5, 6],
        [20, 21, 22, 23, 24, 7],
        [19, 32, 33, 34, 25, 8],
        [18, 31, 36, 35, 26, 9],
        [17, 30, 29, 28, 27, 10],
        [16, 15, 14, 13, 12, 11]
    ]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    assert snail(arr) == expected
