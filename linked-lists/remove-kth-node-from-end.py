class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(1) Space
def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    
    while counter <= k: 
        second = second.next
        counter += 1
        
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    
    while second.next is not None: 
        second = second.next
        first = first.next
        
    first.next = first.next.next 

def main():
    head = LinkedList(0)
    head.next = LinkedList(1)
    head.next.next = LinkedList(2)
    head.next.next.next = LinkedList(3) 
    head.next.next.next.next = LinkedList(4) 
    head.next.next.next.next.next = LinkedList(5) 
    head.next.next.next.next.next.next = LinkedList(6) 
    head.next.next.next.next.next.next.next = LinkedList(7) 
    head.next.next.next.next.next.next.next.next = LinkedList(8) 
    head.next.next.next.next.next.next.next.next.next = LinkedList(9) 

    k = 4
    removeKthNodeFromEnd(head, k)
    print(f'{head.value} -> {head.next.value} -> {head.next.next.value} -> {head.next.next.next.value} -> {head.next.next.next.next.value} -> {head.next.next.next.next.next.value} -> {head.next.next.next.next.next.next.value} -> {head.next.next.next.next.next.next.next.value} -> {head.next.next.next.next.next.next.next.next.value}')
    
if __name__ == "__main__":
    main()