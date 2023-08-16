def findMiddle(head):
    if head is None:
        return None

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow.value
