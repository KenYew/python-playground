class TreeNode:
  def __init__(self, value, left=None, right=None): 
    self.value = value
    self.left = left
    self.right = right

def countPaths(root, targetSum): 
  currentPath = []
  return countPathRecursive(root, targetSum, currentPath)

def countPathRecursive(currentNode, targetSum, currentPath): 
  if currentNode is None: 
    return 0 

  currentPath.append(currentNode.value) 
  pathSum, pathCount = 0, 0 
  for idx in range(len(currentPath) - 1, -1, -1):
    pathSum += currentPath[idx]
    if pathSum == targetSum: 
      pathCount += 1  

  pathCount += countPathRecursive(currentNode.left, targetSum, currentPath)
  pathCount += countPathRecursive(currentNode.right, targetSum, currentPath)

  del currentPath[-1]

  return pathCount

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(countPaths(root, 11)))

if __name__ == "__main__": 
  main()