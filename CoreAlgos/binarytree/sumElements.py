import collections

# iterative


def sum_tree(node):
    if node is None:
        return 0

    sum = 0
    queue = collections.deque([node])
    while queue:
        node = queue.popleft()
        sum += node.value
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return sum

# recursive


def sum_tree_rec(node):
    if not node:
        return 0
    return node.value + sum_tree_rec(node.left) + sum_tree_rec(node.right)
