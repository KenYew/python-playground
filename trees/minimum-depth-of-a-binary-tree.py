from collections import deque
class TreeNode: 
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def findMinimumDepth(root): 
  if root is None: 
    return 0
  minimumDepth = 0
  queue = deque()
  queue.append(root)

  while queue:
    minimumDepth += 1
    levelSize = len(queue)
    for _ in range(levelSize): 
      currentNode = queue.popleft()

      if currentNode.left is None and currentNode.right is None: 
        return minimumDepth
      
      if currentNode.left is not None: 
        queue.append(currentNode.left)
      if currentNode.right is not None: 
        queue.append(currentNode.right)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(findMinimumDepth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(findMinimumDepth(root)))

if __name__ == "__main__":
  main()