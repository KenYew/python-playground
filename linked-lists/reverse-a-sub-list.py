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

def reverseSubList(head, p, q): 
  if p == q: 
    return head

  previous, current = None, head
  idx = 0 
  while current is not None and idx < p - 1: 
    previous = current
    current = current.next
    idx += 1
  
  lastNodeOfFirstPart = previous
  lastNodeOfSubList = current 

  idx = 0 
  while current is not None and idx < q - p + 1:
    next = current.next
    current.next = previous
    previous = current
    current = next 
    idx += 1

  if lastNodeOfFirstPart is not None: 
    lastNodeOfFirstPart.next = previous
  else: 
    head = previous
  
  lastNodeOfSubList.next = current
  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.printList()
  result = reverseSubList(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.printList()

if __name__ == "__main__": 
  main()