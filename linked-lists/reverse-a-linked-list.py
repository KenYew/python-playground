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

def reverse(head): 
  previous, current, next = None, head, None
  while current is not None: 
    next = current.next
    current.next = previous 
    previous = current
    current = next 
  return previous 

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.printList()
  result = reverse(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.printList()

if __name__ == "__main__": 
  main()