from collections import deque
class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def traverse(root): 
  result = []
  if root is None: 
    return result

  queue = deque()
  queue.append(root) 
  isLeftToRight = True

  while queue: 
    currentLevel = deque()
    for _ in range(len(queue)): 
      currentNode = queue.popleft()

      if isLeftToRight: 
        currentLevel.append(currentNode.value)
      else: 
        currentLevel.appendleft(currentNode.value)

      if currentNode.left is not None: 
        queue.append(currentNode.left)
      if currentNode.right is not None: 
        queue.append(currentNode.right)

    result.append(list(currentLevel))
    isLeftToRight = not isLeftToRight
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))

if __name__ == "__main__":
  main()