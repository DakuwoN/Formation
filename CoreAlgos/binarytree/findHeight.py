def tree_height(root: TreeNode) -> int:
    if not root:
        return -1
    return 1 + max(tree_height(root.left), tree_height(root.right))
