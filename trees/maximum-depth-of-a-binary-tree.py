from collections import deque
class TreeNode: 
  def __init__(self, value, left=None, right=None): 
    self.value = value
    self.left = left
    self.right = right

def findMaximumDepth(root): 
  if root is None:
    return 0 

  queue = deque()
  queue.append(root) 
  maximumDepth = 0
  
  while len(queue) > 0: 
    maximumDepth += 1
    levelSize = len(queue)
    for _ in range(levelSize): 
      
      currentNode = queue.popleft()

      if currentNode.left is not None:
        queue.append(currentNode.left)
      if currentNode.right is not None:
        queue.append(currentNode.right)

  return maximumDepth

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Maximum Depth: " + str(findMaximumDepth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Maximum Depth: " + str(findMaximumDepth(root)))

if __name__ == "__main__":
  main()