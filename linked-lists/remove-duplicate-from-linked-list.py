class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    # set the head of the linkedList to be currentNode
    currentNode = linkedList
    # while we haven't traversed until the end of the linkedList
    while currentNode is not None: 
        # set nextDistinctNode to be the pointer of currentNode
        nextDistinctNode = currentNode.next
        # while nextDistinctNode is not the end of the linkedList and comparing the values of next and current nodes,
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            # if values are the same, keep moving the nextDistinctNode pointer until we find a distinct value 
            nextDistinctNode = nextDistinctNode.next 
        
        # change the current node's pointer to be the newly updated nextDistinctNode pointer
        currentNode.next = nextDistinctNode
        # iterate to the next node to repeat the above conditions
        currentNode = nextDistinctNode
    return linkedList     

# This is an input class. Do not edit.
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
    