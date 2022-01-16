def numIslands(grid: List[List[str]]) -> int:
    if not grid: return 0
    r, c = len(grid), len(grid[0])
    visited = [[False for _ in range(c)] for _ in range(r)]

    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0' or visited[i][j]:
            return
        visited[i][j] = True
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

def numIslands(matrix: List[List[str]]) -> int:
    visited = [[False for value in row] for row in matrix]
    numberOfRivers = 0
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
      
    def traverseNode(i, j, matrix, visited, numberOfRivers): 
        nodesToExplore = [[i, j]]

        while len(nodesToExplore) > 0: 
            currentNode = nodesToExplore.pop()
            i, j = currentNode[0], currentNode[1]

            if visited[i][j]:
                continue
            visited[i][j] = True
            if matrix[i][j] == 0:
                continue

            numberOfRivers += 1

            unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visited)
            for neighbour in unvisitedNeighbours:
                nodesToExplore.append(neighbour)
                
        return numberOfRivers

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, numberOfRivers)
    return numberOfRivers