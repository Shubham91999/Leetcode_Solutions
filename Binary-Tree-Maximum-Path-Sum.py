# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Global variable to store max path
        res = [root.val]

        # Helper function dfs to compute max path
        def dfs(root):
            if not root:
                return 0

            max_left = dfs(root.left)
            max_left = max(max_left, 0)

            max_right = dfs(root.right)
            max_right = max(max_right, 0)

            """ Computing max path sum WITH the split, 
            useful incase upper node values are lesser and right child values are greater, 
            so non need of splitting at upper nodes"""
            res[0] = max(res[0], root.val + max_left + max_right)

            # Returning max sum without split because of probability of split in upper nodes for max sum
            return root.val + max(max_left, max_right)

        dfs(root)
        return res[0]