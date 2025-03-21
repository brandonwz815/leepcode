# https://grok.com/chat/1cc9eee2-34a1-4d8b-a746-6052ecbc2b4d

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_tree(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            current = queue.popleft()

            # Process current node (example: print value)
            print(current.val, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        # Optional: Print newline between levels
        print()  # Shows level separation


# Example usage:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("BFS traversal:")
bfs_tree(root)
