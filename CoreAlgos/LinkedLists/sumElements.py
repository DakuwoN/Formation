def sum(node):
    total = 0
    while node is not None:
        total += node.value 
        node = node.next 
    return total 

# Recursive

def sum(node):
    if node is None:
        return 0
    return node.value + sum(node.next)