class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def print(self):
        print(self.value)
        if self.next is not None:
            self.next.print()

    # Iterative
    def count(node):
        length = 0
        while node is not None:
            node = node.next
            length += 1
        return length

    # Recursive
    def count(node):
        if node is None:
            return 0
        return 1 + count(node.next)
