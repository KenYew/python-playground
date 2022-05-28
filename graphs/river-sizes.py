def numberOfIslands(matrix):
  result = []
  visited = [[None for value in row] for row in matrix]
  for i in range(len(matrix)): 
    for j in range(len(matrix[i])): 
      if visited[i][j]: 
        continue
      traverse(i, j, matrix, visited, result)
  return result 

def traverse(i, j, matrix, visited, result): 
  currentRiverSize = 0
  stack = [[i, j]]

  while len(stack) > 0: 
    currentNode = stack.pop()
    i, j = currentNode[0], currentNode[1]

    if visited[i][j]:
      continue
    visited[i][j] = True

    if matrix[i][j] == 0: 
      continue

    currentRiverSize += 1

    if i > 0 and not visited[i - 1][j]:
      stack.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]: 
      stack.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
      stack.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
      stack.append([i, j + 1])
    
  if currentRiverSize: 
    result.append(currentRiverSize)

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
    expected = [2, 1, 5, 2, 2]
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main(argv=[''], verbosity=2, exit=False)