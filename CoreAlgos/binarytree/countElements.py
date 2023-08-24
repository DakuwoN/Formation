import collections
# iterative


def count_tree(node):
    if node is None:
        return 0

    count = 0
    queue = collections.deque([node])

    while queue:
        print(queue)
        count += 1
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count

# recurisve


def count_tree_recursive(node):
    if not node:
        return 0
    return 1 + count_tree_recursive(node.left) + count_tree_recursive(node.right)
