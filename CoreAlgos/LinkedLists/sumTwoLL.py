def sumTwoLL(head1: ListNode, head2: ListNode):
    curr1 = head1
    curr2 = head2
    new_node = new_head = ListNode(0)

    while curr1 or curr2:
        result = 0
        if curr1:
            result += curr1.value
            curr1 = curr1.next
        if curr2:
            result += curr2.value
            curr2 = curr2.next
        new_node.next = ListNode(result)
        new_node = new_node.next

    return new_head.next
