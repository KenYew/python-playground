# O(w.h) Time | O(w.h) Space where w and are the width and height of the input matrix
def removeIslands(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            """
            [x, x, x, x] rowIsBorder: row == 0
            [x, 0, 0, x]
            [x, 0, 0, x]
            [x, x, x, x] rowIsBorder: row == len(matrix) - 1
            colIsBorder:
            col == 0  len(matrix[row]) - 1
            """
            # 1: Evaluate the Booleans below if current element (row, col) constitutes as a border island
            rowIsBorder = (row == 0 or row == len(matrix) - 1)
            colIsBorder = (col == 0 or col == len(matrix[row]) - 1)
            isBorder = (rowIsBorder or colIsBorder)
            
            # 2: Skip iteration if current element is not located at a border
            if not isBorder:
                continue
            
            # 3: Skip iteration if current element is not an island (1)
            if matrix[row][col] != 1:
                continue
            
            # 4: Otherwise, current element is a border island that we need to traverse via iterative DFS
            changeOnesConnectedToBorderToTwos(matrix, row, col)
            
    # 15: After iterative DFS, all islands (1) have been mutated to 2 and we loop through the matrix,
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            color = matrix[row][col]
            # 16: Convert any 1s into 0s as they constitute islands not connected to a border
            if color == 1:
                matrix[row][col] = 0
            # 17: Convert any 2s into 1s as they constitute border islands
            elif color == 2:
                matrix[row][col] = 1
    # 18: Finally, output the mutated matrix in place as the answer
    return matrix

def changeOnesConnectedToBorderToTwos(matrix, startRow, startCol):
    # 5: Initialise a stack of tuples to keep track of all islands to traverse
    stack = [(startRow, startCol)]
    
    # 6: While we haven't finish traversing, pop the stack to evaluate current island
    while len(stack) > 0: 
        currentPosition = stack.pop()
        
        # 7: Unpack the tuple into currentRow and currentCol
        currentRow, currentCol = currentPosition
        
        # 8: Mutate the island value of the matrix in-place from 1 to 2 
        matrix[currentRow][currentCol] = 2
        
        # 9: Then, check neighboring elements for any potential islands
        neighbors = getNeighbors(matrix, currentRow, currentCol)
        
        # 12: Once we've collected a list of valid neighbors to explore, loop through each neighbor 
        for neighbor in neighbors:
            row, col = neighbor # Unpack the (row, col) tuple of current neighbor
            
            # 13: If neighbor is not an island (0), skip iteration
            if matrix[row][col] != 1:
                continue
            
            # 14: Otherwise neighbor is an island (1) and append its tuple (row, col) into the stack 
            # The stack enables LIFO order to perform DFS on all islands
            stack.append(neighbor)
            
def getNeighbors(matrix, row, col):
    # 10: Initialise a list of potential neighbors, depth and width of matrix
    neighbors = []
    numRows = len(matrix)
    numCols = len(matrix[row])
    
    # 11: Append all the (row, col) tuples of valid neighbors into List
    if row - 1 >= 0: # ABOVE
        neighbors.append((row - 1, col))
    if row + 1 < numRows: # BELOW
        neighbors.append((row + 1, col))
    if col - 1 >= 0: # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < numCols: # RIGHT
        neighbors.append((row, col + 1))
        
    return neighbors

matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]
print(removeIslands(matrix))

