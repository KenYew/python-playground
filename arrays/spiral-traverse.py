array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]

def spiralTraverse(array):
    startRow, endRow = 0, len(array) - 1 # Iteration 1: 0, 3
    startCol, endCol = 0, len(array[0]) - 1 # Iteration 1: 0, 3
    ans = []
    
    while startRow <= endRow and startCol <= endCol: 
        for col in range(startCol, endCol + 1): # Iteration 1: 0, 4 (0 -> 3) Iteration 2: 1, 3 (1 -> 2)
            ans.append(array[startRow][col])
        for row in range(startRow + 1, endRow + 1): # Iteration 1: 1, 4 (1 -> 3) Iteration 2: 2, 3 (2)
            ans.append(array[row][endCol])
        for col in reversed(range(startCol, endCol)): # Iteration 1: 3, 0 (2 -> 0) Iteration 2: 2, 1 (1)
            if startRow == endRow: # Handle the edge case when there's a single row in the middle of the matrix. In this case, we don't want to double-count the values in this row, which we've already counted in the first for loop above.
                break
            ans.append(array[endRow][col])
        for row in reversed(range(startRow + 1, endRow)): # Iteration 1: 3, 1 (2 -> 1) Iteration 2:  2, 2 (BREAK)
            if startCol == endCol: # Handle the edge case when there's a single column in the middle of the matrix. In this case, we don't want to double-count the values in this column, which we've already counted in the second for loop above.
                break
            ans.append(array[row][startCol])
        startRow += 1 # Value Updated: 1
        endRow -= 1 # Value Updated: 2
        startCol += 1 # Value Updated: 1
        endCol -= 1 # Value Updated: 2
        
    return ans

print(spiralTraverse(array))

startCol, endCol = 0, len(array[0]) - 1
for i in reversed(range(startCol, endCol)):
    print(f'Range: {i} Value: {array[0][i]}')