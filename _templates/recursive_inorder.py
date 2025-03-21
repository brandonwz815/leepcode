# https://grok.com/chat/7aeacdbf-df33-4c25-9c77-be4170ed5c2e


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ") # process root node
        inorder_traversal(root.right)
