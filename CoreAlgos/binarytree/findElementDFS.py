# iterative

def find_dfs(node: TreeNode, target: int) -> int:
    if not node:
        return False

    stack = [node]
    while stack:
        curr = stack.pop()
        if curr.value == target:
            return True
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    return False

# recursion


def sum_tree_rec(node: TreeNode) -> int:
    if not node:
        return 0
    return node.value + sum_tree_rec(node.left) + sum_tree_rec(node.right)
