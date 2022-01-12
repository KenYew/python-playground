# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(1) Space - where n is the number of nodes in the linked list
def reverseLinkedList(head):
    previous, current = None, head
    while current is not None: 
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

def main():
    head = LinkedList(0)
    head.next = LinkedList(1)
    head.next.next = LinkedList(2)
    head.next.next.next = LinkedList(3) 
    head.next.next.next.next = LinkedList(4) 
    head.next.next.next.next.next = LinkedList(5) 

    reversedHead = reverseLinkedList(head)
    print(f'{reversedHead.value} -> {reversedHead.next.value} -> {reversedHead.next.next.value} -> {reversedHead.next.next.next.value} -> {reversedHead.next.next.next.next.value} -> {reversedHead.next.next.next.next.next.value}')
    
if __name__ == "__main__":
    main()