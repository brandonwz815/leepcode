# https://grok.com/chat/ced5ed8b-144a-4cbe-a6d5-f1ec8ad6e28a


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_iterative(root):
    if not root:
        return []

    result = []

    stack = [root]

    while stack:
        current = stack.pop()

        # Add current node's value to result
        result.append(current.value)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return result


# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Get preorder traversal
    result = preorder_iterative(root)
    print("Preorder traversal:", result)  # Output: [1, 2, 4, 5, 3]
