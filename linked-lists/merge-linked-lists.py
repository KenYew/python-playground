class ListNode: 
  def __init__(self, value=0, next=None): 
    self.value = value
    self.next = next

def mergeTwoLists(list1, list2): 
  head = current = ListNode()
  while list1 is not None and list2 is not None: 
    if list1.value < list2.value: 
      current.next = list1
      list1 = list1.next
    else: 
      current.next = list2
      list2 = list2.next
    current = current.next
  if list1 is not None: 
    current.next = list1
  elif list2 is not None: 
    current.next = list2
  return head.next

import unittest
class UnitTest(unittest.TestCase): 
  def getList(self, node): 
    result = []
    currentNode = node
    while currentNode is not None: 
      result.append(currentNode.value)
      currentNode = currentNode.next
    return result 

  def testCase(self): 
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    actual = self.getList(mergeTwoLists(list1, list2))
    expected = [1, 1, 2, 3, 4, 4]
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main(argv=[''], verbosity=2, exit=False)