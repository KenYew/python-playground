def maxAreaOfIsland(self, grid):
    seen = set()
    ans = 0
    for r0, row in enumerate(grid):
        for c0, val in enumerate(row):
            if val and (r0, c0) not in seen:
                shape = 0
                stack = [(r0, c0)]
                seen.add((r0, c0))
                while stack:
                    r, c = stack.pop()
                    shape += 1
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                and grid[nr][nc] and (nr, nc) not in seen):
                            stack.append((nr, nc))
                            seen.add((nr, nc))
                ans = max(ans, shape)
    return ans

# OR 

def riverSizes(matrix):
    visited = [[False for value in row] for row in matrix]
    sizes = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return max(sizes) if len(sizes) > 0 else 0
    
def traverseNode(i, j, matrix, visited, sizes): 
    currentRiverSize = 0 
    nodesToExplore = [[i, j]]
    
    while len(nodesToExplore) > 0: 
        currentNode = nodesToExplore.pop()
        i, j = currentNode[0], currentNode[1]
        
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue

        currentRiverSize += 1
        
        unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visited)
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour)
            
    if currentRiverSize > 0: 
        sizes.append(currentRiverSize)
        
def getUnvisitedNeighbours(i, j, matrix, visited): 
    unvisitedNeighbours = []
    
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbours.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbours.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbours.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbours.append([i, j + 1])
    
    return unvisitedNeighbours    