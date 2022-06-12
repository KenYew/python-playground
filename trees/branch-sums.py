"""
tree =
                 1
              /    \
            2        3
           /  \     /  \
         4     5   6    7 
        / \    /
       8   9  10
Output: [15, 16, 18, 10, 11]
15 == 1 + 2 + 4 + 8
16 == 1 + 2 + 4 + 9
18 == 1 + 2 + 5 + 10
10 == 1 + 3 + 6
11 == 1 + 3 + 7
"""
class TreeNode:
  def __init__(self, value=0, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
      
def branchSums(root):
  result = []
  branchSumsRecursive(root, 0, result)
  return result

def branchSumsRecursive(currentNode, currentSum, result):
  if currentNode is None:
    return
  
  currentSum += currentNode.value
  
  if currentNode.left is None and currentNode.right is None: 
    result.append(currentSum)
    
  branchSumsRecursive(currentNode.left, currentSum, result)
  branchSumsRecursive(currentNode.right, currentSum, result)
  
  currentSum -= currentNode.value

import unittest
class UnitTest(unittest.TestCase):
  def testCase(self):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    actual = branchSums(root)
    expected = [15, 16, 18, 10, 11]
    self.assertEqual(actual, expected)
    
if __name__ == '__main__':
  unittest.main(verbosity=2, exit=False)