class TreeNode: 
  def __init__(self, value, left=None, right=None): 
    self.value = value
    self.left = left
    self.right = right

def isSameTree(node1, node2): 
  if node1 is None or node2 is None: 
    return node1 == node2

  if node1.value != node2.value: 
    return False

  return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)
               
def main(): 
  node1 = TreeNode(1)
  node1.left = TreeNode(2)
  node1.right = TreeNode(3)
  node2 = TreeNode(1)
  node2.left = TreeNode(2)
  node2.right = TreeNode(3)
  print(isSameTree(node1, node2))

  node1 = TreeNode(1)
  node1.left = TreeNode(2)
  node1.right = TreeNode(1)
  node2 = TreeNode(1)
  node2.left = TreeNode(1)
  node2.right = TreeNode(2)
  print(isSameTree(node1, node2))

if __name__ == "__main__":
  main()