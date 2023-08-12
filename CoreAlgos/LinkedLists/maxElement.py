def findMax(node):
    curr_max = node.value 
    while node is not None:
        curr_max = max(curr_max, node.value)
        node = node.next 
    return curr_max 

#Recurisve 
def findMax(node):
    if node.next is None:
        return node.value 
    return max(node.value, findMax(node.next))