# O(n) Time - we only need to traverse all of the elements in the matrix once
# O(n) Space - we are using an auxiliary matrix of size n to keep track of visited nodes
# n - the number of elements in the matrix
def riverSizes(matrix):
    sizes = [] # answer array
    # Auxiliary matrix to keep track of nodes that already been visited
    visited = [[False for value in row] for row in matrix] 
    for i in range(len(matrix)): # for every row,
        for j in range(len(matrix[i])): # for every column,
            if visited[i][j]: # if node is already marked as visited in our auxiliary matrix, we skip it
                continue
            traverseNode(i, j, matrix, visited, sizes) # otherwise if unvisited, traverse node at position (i, j)
    return sizes

def traverseNode(i, j, matrix, visited, sizes): 
    currentRiverSize = 0 # initializing a potentially new river
    # ==============================
    # Depth First Search (Iterative)
    # ==============================
    nodesToExplore = [[i, j]] # stack of nodes to explore (Iterative DFS implementation)

    # STEP 1: EXPLORE NODES, USE STACK AND ITERATE DFS ON POPPED NODES THAT ARE RIVERS (1's)
    while len(nodesToExplore): # while we still have nodes to explore,
        currentNode = nodesToExplore.pop() # pop out the final value of the nodesToExplore array
        i, j = currentNode[0], currentNode[1]

        # STEP 2: SKIP IF ALREADY VISITED OR LAND
        if visited[i][j]: # if node has already been visited, we skip it
            continue
        visited[i][j] = True # otherwise if not visited, mark the current node being traversed as visited to keep track
        if matrix[i][j] == 0: # if it is a piece of land, we skip it
            continue

        # STEP 3: OTHERWISE, WE FOUND A RIVER!
        currentRiverSize += 1

        # STEP 4: NOW, CHECK ADJACENT NEIGHBOURS AND ITERATE DFS ON NEWLY APPENDED NEIGHBOUR NODES THAT ARE RIVERS
        unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visited) # get unvisited neighbours around our current node and add it to nodesToExplore stack
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour) # append new unvisited neighbours to explore in the stack

    # STEP 5: AFTER FULLY TRAVERSING, APPEND ANSWER TO OUR RIVER SIZES ARRAY
    if currentRiverSize > 0: # if we have an actual river, we append to our sizes answer array
        sizes.append(currentRiverSize)
    
def getUnvisitedNeighbours(i, j, matrix, visited):
    unvisitedNeighbours = []
    # Check if the 4 surrounding adjacent neighbours are valid neighbours (unvisited and within the matrix boundary)
    # ==========================================
    # ROWS CHECK FOR NEIGHBOURS ABOVE AND BELOW
    # ==========================================
    if i > 0 and not visited[i - 1][j]: # if we are not in the top row and not visited the neighbour above,
        unvisitedNeighbours.append([i - 1, j]) # append the node (with indices) of the neighbour above us
    if i < len(matrix) - 1 and not visited[i + 1][j]: # if we are not in the bottomw row and not visited neighbour below,
        unvisitedNeighbours.append([i + 1, j]) # append the node (with indices) of the neighbour below us
    # ============================================
    # COLUMNS CHECK FOR NEIGHBOURS LEFT AND RIGHT
    # ============================================
    if j > 0 and not visited[i][j - 1]: # if we are not in the left-most column and not visited the neighbour to the left,
        unvisitedNeighbours.append([i, j - 1]) # append the node (with indices) of the left neighbour
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]: # if we are not in the right-most column and not visited the neighbour to the right, 
        unvisitedNeighbours.append([i, j + 1]) # append the node (with indices) of the right neighbour
    return unvisitedNeighbours # finally, return the array containing nodes of all unvisited adjacent neighbours