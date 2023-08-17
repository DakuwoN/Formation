def reverse(head):
    prev = None
    curr = head
    while curr is not None:
        (curr.next, curr, prev) = (prev, curr.next, curr)
    return prev
