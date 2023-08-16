def remove(head: ListNode, target):
    sentinel = ListNode(0)
    sentinel.next = head
    curr = sentinel

    while curr.next is not None:
        if curr.next.target == target:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return sentinel.next

# Recursive


def remove(head: ListNode, target):
    if head is None:
        return None

    head.next = remove(head.next, target)
    if target == head.target:
        return head.next
    return head
