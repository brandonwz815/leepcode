# https://grok.com/chat/0e9584b8-a746-481d-a5ef-7aeea6ac5744


# Assuming a basic binary tree node structure
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Preorder traversal function
def preorder(node):
    # Base case: if node is None, return
    if node is None:
        return

    print(node.value, end=" ")  # Or any processing you want

    preorder(node.left)

    preorder(node.right)


# Example usage
if __name__ == "__main__":
    # Create a sample tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Call preorder traversal
    print("Preorder traversal:")
    preorder(root)  # Output: 1 2 4 5 3
