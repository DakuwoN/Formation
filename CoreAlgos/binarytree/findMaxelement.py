# iterative
import collections


def tree_max(node: TreeNode) -> int:
    if not node:
        return float("-inf")
    max_value = 0
    queue = collections.deque([node])
    while queue:
        node = queue.popleft()
        max_value = max(max_value, node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return max_value

# recursion


def tree_max(node):
    if not node:
        return float("-inf")
    return max(node.value, tree_max(node.left), tree_max(node.right))
