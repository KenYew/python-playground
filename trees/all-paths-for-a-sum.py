class TreeNode:
  def __init__(self, value=0, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def findPaths(root, targetSum):
  currentPath, allPaths = [], []
  findPathsRecursive(root, targetSum, currentPath, allPaths)
  return allPaths

def findPathsRecursive(currentNode, currentSum, currentPath, allPaths): 
  if currentNode is None:
    return 
  
  currentPath.append(currentNode.value) 
  
  if currentSum == currentNode.value and currentNode.left is None and currentNode.right is None:
    allPaths.append(list(currentPath))
    
  currentSum -= currentNode.value
  
  findPathsRecursive(currentNode.left, currentSum, currentPath, allPaths)
  findPathsRecursive(currentNode.right, currentSum, currentPath, allPaths)
  
  currentPath.pop()

import unittest
class UnitTest(unittest.TestCase):
  def testCase(self): 
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    requiredSum = 23
    print("Tree paths with requiredSum " + str(requiredSum) +
    ": " + str(findPaths(root, requiredSum)))
    actual = findPaths(root, requiredSum)
    expected = [[12, 7, 4], [12, 1, 10]]
    self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()