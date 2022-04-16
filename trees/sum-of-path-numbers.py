class TreeNode:
  def __init__(self, value): 
    self.value = value
    self.left = None
    self.right = None

def findPathSum(root):
  pathSum = 0
  return findPathSumRecursive(root, pathSum)

# O(n) Time - where n is the total number of nodes in the tree
# We traverse each node once. 
# O(n) Space worst case - where n is the total number of nodes in the tree that will be stored in the recursion stack
# Worst case is when the given tree is a linked list where every node has only one child
def findPathSumRecursive(currentNode, pathSum): 
  if currentNode is None: 
    return 0
  
  pathSum = 10 * pathSum + currentNode.value

  if currentNode.left is None and currentNode.right is None: 
    return pathSum 
  
  return findPathSumRecursive(currentNode.left, pathSum) + findPathSumRecursive(currentNode.right, pathSum)

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(findPathSum(root)))

if __name__ == "__main__":
  main()