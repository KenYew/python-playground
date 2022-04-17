from collections import deque 
class TreeNode: 
  def __init__(self, value, left=None, right=None, next=None): 
    self.value = value 
    self.left = left 
    self.right = right
    self.next = next 

  def printLevelOrder(self): 
    nextLevelRoot = self 
    while nextLevelRoot is not None: 
      currentNode = nextLevelRoot
      nextLevelRoot = None 
      while currentNode is not None: 
        print(f'{str(currentNode.value)} ', end='')
        if not nextLevelRoot: 
          if currentNode.left is not None: 
            nextLevelRoot = currentNode.left
          elif currentNode.right is not None: 
            nextLevelRoot = currentNode.right
        currentNode = currentNode.next
      print()

def connectLevelOrderSiblings(root):
  if root is None:
    return
  
  queue = deque()
  queue.append(root)

  while len(queue) > 0: 
    previousNode = None
    levelSize = len(queue)

    for _ in range(levelSize): 
      currentNode = queue.popleft()

      if previousNode is not None: 
        previousNode.next = currentNode
      previousNode = currentNode

      if currentNode.left is not None: 
        queue.append(currentNode.left)
      if currentNode.right is not None: 
        queue.append(currentNode.right)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connectLevelOrderSiblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.printLevelOrder()

if __name__ == "__main__":
  main()