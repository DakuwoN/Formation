def insert_bst(root: TreeNode, target: int) -> TreeNode:
    if not root:
        return TreeNode(target)
    curr = root
    while curr:
        if curr.value < target:
            if curr.right:
                curr = curr.right
            else:
                curr.right = TreeNode(target)
                return root
        else:
            if curr.left:
                curr = curr.left
            else:
                curr.left = TreeNode(target)
                return root
