from collections import deque


def find_bfs(node: TreeNode, target: int) -> bool:
    if not node:
        return False

    # We use a deque so we can pop the leftmost element in O(1)
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        if curr.value == target:
            return True
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return False
