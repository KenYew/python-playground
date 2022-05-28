class TreeNode: 
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right 

def isSymmetric(root):
  if root is None:
    return True
  return isSymmetricRecursion(root.left, root.right)

def isSymmetricRecursion(leftNode, rightNode): 
  if leftNode is None and rightNode is None:
    return True
  if leftNode is None or rightNode is None:
    return False

  if leftNode.value == rightNode.value: 
    outerPair = isSymmetricRecursion(leftNode.left, rightNode.right)
    innerPair = isSymmetricRecursion(leftNode.right, rightNode.left)
    return innerPair and outerPair
  else:
    return False
  
def main(): 
  tree1 = TreeNode(1)
  tree1.left = TreeNode(2)
  tree1.left.left = TreeNode(3)
  tree1.left.right = TreeNode(4)
  tree1.right = TreeNode(2)
  tree1.right.left = TreeNode(4)
  tree1.right.right = TreeNode(3)

  tree2 = TreeNode(1)
  tree2.left = TreeNode(2)
  tree2.left.right = TreeNode(3)
  tree2.right = TreeNode(2)
  tree2.right.right = TreeNode(3)
  print(isSymmetric(tree1))
  print(isSymmetric(tree2))

if __name__ == "__main__":
  main()