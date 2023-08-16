def remove(head: ListNode, value):
    sentinel = ListNode(0)
    sentinel.next = head 
    curr = sentinel 
    
    while curr.next is not None:
        if curr.next.value == value:
            curr.next = curr.next.next 
        else:
            curr = curr.next 
    return sentinel.next 

#Recursive 

def remove(head: ListNode, value):
    if head is None:
        return None 
    
    head.next = remove(head.next, value)
    if value == head.value:
        return head.next 
    return head 
    