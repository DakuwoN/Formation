def insert(head: ListNode, value):
    if head is None:
        return ListNode(value)

    dummy_head = ListNode(0)
    dummy_head.next = head
    node = dummy_head

    while node:
        if not node.next or value < node.next.value:
            next = node.next
            node.next = ListNode(value)
            node.next.next = next
            break
        node = node.next

    return dummy_head.next

# Recursive


def insert(head: ListNode, value):
    newNode = ListNode(value)

    if head is None:
        return newNode

    if value < head.value:
        newNode.next = head
        return newNode

    if head.next is None:
        head.next = newNode
    else:
        head.next = insert(head.next, value)

    return head
