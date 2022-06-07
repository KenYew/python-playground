def numberOfIslands(matrix): 
    if not matrix:
        return 0
    result = 0
    visited = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not visited[i][j] and matrix[i][j] == 1: 
                dfs(i, j, matrix, visited)
                result += 1
    return result

def dfs(i, j, matrix, visited): 
    if visited[i][j] or matrix[i][j] == 0:
        return
    visited[i][j] = True
    
    if i > 0 and not visited[i - 1][j]: 
        dfs(i - 1, j, matrix, visited)
    if i < len(matrix) - 1 and not visited[i + 1][j]: 
        dfs(i + 1, j, matrix, visited)
    if j > 0 and not visited[i][j - 1]: 
        dfs(i, j - 1, matrix, visited)
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]: 
        dfs(i, j + 1, matrix, visited)
        
import unittest
class UnitTest(unittest.TestCase):
  def testCase(self): 
    matrix = [
      [1, 0, 0, 1, 0],
      [1, 0, 1, 0, 0],
      [0, 0, 1, 0, 1],
      [1, 0, 1, 0, 1],
      [1, 0, 1, 1, 0]
    ]
    actual = numberOfIslands(matrix)
    expected = 5
    self.assertEqual(actual, expected)
    
if __name__ == '__main__':
  unittest.main(verbosity=2, exit=False)