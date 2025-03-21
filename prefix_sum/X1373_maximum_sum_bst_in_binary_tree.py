# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/description/
# https://chatgpt.com/c/67b721ee-6564-8001-905a-652fb9f921c5
# https://grok.com/chat/d3d5d195-e54a-48f5-b31f-5218a1a76636


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 关键：空子树是 BST, 考虑 min(left_min, node.val) 和 max(node.val, right_max)
    
    def maxSumBST(self, root):
        self.max_sum = 0  # Global variable to store max sum

        def dfs(node):
            if not node:
                return (True, float("inf"), float("-inf"), 0)  # isBST, min, max, sum

            left_isBST, left_min, left_max, left_sum = dfs(node.left)
            right_isBST, right_min, right_max, right_sum = dfs(node.right)

            # Check if the current subtree is a BST
            if left_isBST and right_isBST and left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, curr_sum)
                return (
                    True,
                    min(left_min, node.val),
                    max(right_max, node.val),
                    curr_sum,
                )
            else:
                return (False, 0, 0, 0)  # Mark subtree as invalid BST

        dfs(root)
        return self.max_sum


if __name__ == "__mani__":
    solution = Solution()
    print(solution.maxSumBST())


"""
Time Complexity: O(N), since each node is visited once.
Space Complexity: O(H), where H is the height of the tree (worst-case O(N) for a skewed tree, best-case O(logN) for a balanced tree.
"""
