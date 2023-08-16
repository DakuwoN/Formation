def search(head: ListNode, target):
    curr = head
    while curr:
        if curr.value == target:
            return True
        curr = curr.next
    return False

# Recursive


def search(head: ListNode, target):
    if head is None:
        return False
    return head.value == target or search(head.next, target)
