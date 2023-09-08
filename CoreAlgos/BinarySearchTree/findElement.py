def search_bst(node: TreeNode, target: int) -> bool:
    curr = node
    while curr:
        if curr.value == target:
            return True
        if curr.value < target:
            curr = curr.right
        else:
            curr = curr.left
    return False
