from collections import deque
class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
    
# O(n) Time - where n is the total number of nodes in the tree
# We traverse each node once. 
# O(n) Space worst case - where n is the total number of nodes in the tree
# We need to return a list containing the level order traversal
# We also need O(n) for the queue. We can have a max of n/2 nodes at any level (at the lowest level of BT)
def findSuccessor(root, key):
  if root is None:
    return None 
  
  queue = deque()
  queue.append(root) 
  
  while len(queue) > 0: 
    currentNode = queue.popleft()
    # We will not keep track of all the levels. 
    # Instead we will keep inserting child nodes to the queue.
    if currentNode.left is not None: 
      queue.append(currentNode.left)
    if currentNode.right is not None: 
      queue.append(currentNode.right)

    # As soon as we find the given node, we will return the next node from the queue as the level order successor.
    if currentNode.value == key: 
      break
  return queue[0] if queue else None

def main():
  root = TreeNode(1);
  root.left = TreeNode(2);
  root.right = TreeNode(3);
  root.left.left = TreeNode(4);
  root.left.right = TreeNode(5);
  
  result = findSuccessor(root, 3)
  if result:
    print(result.value)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  
  result = findSuccessor(root, 9)
  if result:
    print(result.value)
  
  result = findSuccessor(root, 12)
  if result:
    print(result.value)

if __name__ == "__main__": 
  main()