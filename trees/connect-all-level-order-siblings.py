from collections import deque


class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def printTree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.value) + " ", end='')
      current = current.next

def connectAllSiblings(root):
  if root is None:
    return

  queue = deque()
  queue.append(root) 
  currentNode, previousNode = None, None
  while len(queue) > 0: 
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
  connectAllSiblings(root)
  root.printTree()


main()