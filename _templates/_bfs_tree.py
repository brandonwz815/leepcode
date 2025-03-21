from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs_tree(node):
  if not node:
    return
  
  queue=deque([node])

  while queue:
    n = len(queue)

    for i in range(n):
      curNode = queue.popleft()

      # process curNode
      print(curNode.val, end=" ")

      if curNode.left:
         queue.append(curNode.left)
      if curNode.right:
         queue.append(curNode.right)
    print()

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