class TreeNode: 
  def __init__(self, value): 
    self.value = value 
    self.left = None
    self.right = None 

def findPathSum(root, sequence): 
  sequenceIdx = 0
  if not root: 
    return len(sequence) == 0
  return findPathSumRecursive(root, sequence, sequenceIdx)

def findPathSumRecursive(currentNode, sequence, sequenceIdx): 
  if currentNode is None: 
    return False 
  
  sequenceLength = len(sequence)
  if sequenceIdx >= sequenceLength or currentNode.value != sequence[sequenceIdx]: 
    return False

  if sequenceIdx == sequenceLength - 1 and currentNode.left is None and currentNode.right is None: 
    return True

  return findPathSumRecursive(currentNode.left, sequence, sequenceIdx + 1) or findPathSumRecursive(currentNode.right, sequence, sequenceIdx + 1)                       

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(findPathSum(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(findPathSum(root, [1, 1, 6])))

if __name__ == "__main__":
  main()                                                          