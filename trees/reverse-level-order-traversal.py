from collections import deque
class TreeNode: 
  def __init__(self, value, left=None, right=None): 
    self.value = value
    self.left = left
    self.right = right

def traverse(root):
  result = deque()
  if root is None: 
    return result

  queue = deque()
  queue.append(root)

  while queue: 
    levelSize = len(queue)
    currentLevel = []
    for _ in range(levelSize): 
      currentNode = queue.popleft() 
      currentLevel.append(currentNode.value)

      if currentNode.left is not None:
        queue.append(currentNode.left)
      if currentNode.right is not None:
        queue.append(currentNode.right)

    result.appendleft(currentLevel)

  return list(result)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))

if __name__ == "__main__":
  main()