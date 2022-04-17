from collections import deque
class TreeNode: 
  def __init__(self, value, left=None, right=None): 
    self.value = value
    self.left = left
    self.right = right

def treeRightView(root): 
  result = []
  if root is None:
    return

  queue = deque()
  queue.append(root) 

  while len(queue) > 0: 
    levelSize = len(queue)
    for idx in range(levelSize): 
      currentNode = queue.popleft()
      if idx == levelSize - 1: 
        result.append(currentNode)

      if currentNode.left is not None: 
        queue.append(currentNode.left)
      if currentNode.right is not None: 
        queue.append(currentNode.right)
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = treeRightView(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.value) + " ", end='')

if __name__ == "__main__":
  main()