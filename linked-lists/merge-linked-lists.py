class LinkedList: 
    def __init__(self, value):
        self.value = value
        self.next = None
        
def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
    p1Prev = None
    p2 = headTwo
    
    while p1 is not None and p2 is not None: 
        if p1.value < p2.value:
            p1Prev = p1
            p1 = p1.next
        else: 
            if p1Prev is not None: 
                p1Prev.next = p2
            p1Prev = p2
            p2 = p2.next
            p1Prev.next = p1
    
    if p1 is None: 
        p1Prev.next = p2
    return headOne if headOne.value < headTwo.value else headTwo

def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next