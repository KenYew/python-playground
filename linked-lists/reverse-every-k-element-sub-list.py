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

def reverseEveryKElements(head, k): 
  if k <= 1 or head is None: 
    return head

  previous, current = None, head
  while True: 
    lastNodeOfPreviousPart = previous
    lastNodeOfSubList = current
    next = None

    idx = 0
    while current is not None and idx < k: 
      next = current.next
      current.next = previous
      previous = current
      current = next 
      idx += 1

    if lastNodeOfPreviousPart is not None: 
      lastNodeOfPreviousPart.next = previous
    else:
      head = previous 

    lastNodeOfSubList.next = current 

    if current is None: 
      break
    previous = lastNodeOfSubList
  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.printList()
  result = reverseEveryKElements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.printList()

if __name__ == "__main__": 
  main()