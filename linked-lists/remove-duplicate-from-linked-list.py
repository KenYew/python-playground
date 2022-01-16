
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None: 
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = currentNode.next
        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    return linkedList
    