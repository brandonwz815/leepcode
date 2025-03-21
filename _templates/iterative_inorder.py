# https://grok.com/chat/f61984ba-8ba1-45f0-96f5-ccc41a2792e8


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(node):
    result = []
    
    stack = []
    current = node

    while stack or current:
        
        # Traverse to the leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Process current node
        current = stack.pop()
        result.append(current.val)

        # Move to right subtree
        current = current.right

    return result


# Example usage:
#     1
#    / \
#   2   3
#  / \
# 4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inorderTraversal(root))  # Output: [4, 2, 5, 1, 3]
