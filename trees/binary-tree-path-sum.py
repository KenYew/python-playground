class TreeNode: 
  def __init__(self, value): 
    self.value = value 
    self.left = None
    self.right = None

# O(n) Time - where n is the total number of nodes in the tree.
# We need to traverse each node once.
# O(n) Space worst case - where n is the total number of nodes in the tree that will be stored in the recursion stack
# Worst case is when the given tree is a single linked list (where every node has only one child)
def hasPath(currentNode, requiredSum): 
  if currentNode is None: 
    return False
  currentSum = requiredSum - currentNode.value
  if currentNode.value == requiredSum and currentNode.left is None and currentNode.right is None: 
    return True
  return hasPath(currentNode.left, currentSum) or hasPath(currentNode.right, currentSum)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(hasPath(root, 23)))
  print("Tree has path: " + str(hasPath(root, 16)))

if __name__ == "__main__":
  main()