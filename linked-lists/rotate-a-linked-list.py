class Node: 
  def __init__(self, value, next=None): 
    self.value = value
    self.next = next 

  def printList(self):
    node = self
    while node is not None:
      print(node.value, end=" ")
      node = node.next
    print()

def rotateLinkedList(head, rotations): 
  if head is None or head.next is None or rotations <= 0: 
    return head
  
  lastNode = head 
  listLength = 1
  while lastNode.next is not None: 
    lastNode = lastNode.next
    listLength += 1

  lastNode.next = head
  rotations %= listLength
  skipLength = listLength - rotations
  lastNodeOfRotatedList = head

  for idx in range(skipLength - 1): 
    lastNodeOfRotatedList = lastNodeOfRotatedList.next

  head = lastNodeOfRotatedList.next
  lastNodeOfRotatedList.next = None 
  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.printList()
  result = rotateLinkedList(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.printList()

if __name__ == "__main__":
  main()