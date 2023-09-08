def validate_bst(node: TreeNode) -> bool:
    return helper(node, -float('inf'), float('inf'))


def helper(node: TreeNode, min: int, max: int) -> bool:
    if not node:
        return True
    if node.value <= min or node.value > max:
        return False
    return helper(node.left, min, node.value) and helper(node.right, node.value, max)
