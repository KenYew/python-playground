from collections import deque
class TreeNode:
  def __init__(self, value, left=None, right=None): 
    self.value = value
    self.left = left
    self.right = right

def findMaxValues(root): 
  result = []
  if root is None: 
    return result 

  queue = deque()
  queue.append(root) 

  while queue:  
    levelSize = len(queue)
    maxValue = 0
    for _ in range(levelSize): 
      currentNode = queue.popleft()
      maxValue = max(maxValue, currentNode.value)

      if currentNode.left is not None: 
        queue.append(currentNode.left)
      if currentNode.right is not None: 
        queue.append(currentNode.right)

    result.append(maxValue)
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level maxes are: " + str(findMaxValues(root)))

if __name__ == "__main__":
  main()