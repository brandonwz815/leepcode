# https://grok.com/chat/cb2d214b-5e1e-4661-b249-dbe1c0f8d930


def postorder_iterative(root):
    if not root:
        return []

    result = []
    stack = [root]
    visited = set()

    while stack:
        node = stack[-1]  # peek at top of stack

        # Check if we can process current node
        left_done = not node.left or node.left in visited
        right_done = not node.right or node.right in visited

        if left_done and right_done:
            result.append(node.val)
            visited.add(node)
            stack.pop()
        else:
            # Push right child first (if exists and not visited)
            if node.right and node.right not in visited:
                stack.append(node.right)
            # Push left child second (if exists and not visited)
            if node.left and node.left not in visited:
                stack.append(node.left)

    return result
