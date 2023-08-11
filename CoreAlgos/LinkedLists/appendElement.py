def append(head: ListNode, value):
    if head is None:
        return ListNode(value)

    curr = head
    while curr.next is not None:
        curr = curr.next

    curr.next = ListNode(value)
    return head

# Recursive


def append(head: ListNode, value):
    if head is None:
        return ListNode(value)

    if head.next is None:
        head.next = ListNode(value)
    else:
        append(head.next, value)

    return head
