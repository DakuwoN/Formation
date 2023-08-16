def kthFromLast(head: ListNode, k):
    if head is None:
        return None

    slow = head
    fast = head

    for i in range(k):
        if fast is not None:
            fast = fast.next
        else:
            return -1

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow.value
