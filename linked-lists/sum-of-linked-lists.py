class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n, m)) Time | O(max(n, m)) Space
# where n is the length of linkedListOne
# where m is the length of linkedListTwo
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    initialDummyNode = LinkedList(0)
    currentNode = initialDummyNode
    carry = 0
    
    nodeOne, nodeTwo = linkedListOne, linkedListTwo
    
    while nodeOne is not None or nodeTwo is not None or carry != 0: 
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        
        # Arithmetics
        sumOfValues = valueOne + valueTwo + carry
        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        carry = sumOfValues // 10
        
        # Update linked list
        currentNode.next = newNode
        currentNode = newNode
        
        # Traverse linked list
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None
        
    return initialDummyNode.next
        
	
def main():
    linkedListOne = LinkedList(2)
    linkedListOne.next = LinkedList(4)
    linkedListOne.next.next = LinkedList(7)
    linkedListOne.next.next.next = LinkedList(1) 

    linkedListTwo = LinkedList(9)
    linkedListTwo.next = LinkedList(4)
    linkedListTwo.next.next = LinkedList(5)

    print(f'{sumOfLinkedLists(linkedListOne, linkedListTwo).value} -> {sumOfLinkedLists(linkedListOne, linkedListTwo).next.value} -> {sumOfLinkedLists(linkedListOne, linkedListTwo).next.next.value} -> {sumOfLinkedLists(linkedListOne, linkedListTwo).next.next.next.value}')
    
if __name__ == "__main__":
    main()