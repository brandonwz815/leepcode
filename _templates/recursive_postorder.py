# https://grok.com/chat/04cb529e-692f-476b-8206-fe753803ebcb


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def postorder(node):
    # Base case: if node is None, return
    if node is None:
        return

    postorder(node.left)

    postorder(node.right)

    # Process current node
    print(node.value, end=" ")  # Or any other processing


# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Postorder traversal:")
    postorder(root)  # Output: 4 5 2 3 1
