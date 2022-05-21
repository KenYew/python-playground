class TreeNode: 
  def __init__(self, value): 
    self.value = value 
    self.left = None
    self.right = None

def findPaths(root, requiredSum): 
  allPaths = []
  currentPath = []
  currentSum = 0
  findPathsRecursive(root, requiredSum, currentPath, allPaths)
  return allPaths

def findPathsRecursive(currentNode, runningSum, currentPath, allPaths): 
  if currentNode is None: 
    return
  
  currentPath.append(currentNode.value)

  if currentNode.value == runningSum and currentNode.left is None and currentNode.right is None: 
    allPaths.append(list(currentPath))

  currentSum = runningSum - currentNode.value
  findPathsRecursive(currentNode.left, currentSum, currentPath, allPaths)
  findPathsRecursive(currentNode.right, currentSum, currentPath, allPaths)

  del currentPath[-1]

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  requiredSum = 23
  print("Tree paths with requiredSum " + str(requiredSum) +
        ": " + str(findPaths(root, requiredSum)))

if __name__ == "__main__":
  main()