# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 1

        def dfs(root, cur_max):
            nonlocal count 
            if not root:
                return
            if root.val >= cur_max:
                count += 1
                cur_max = root.val

            dfs(root.left, cur_max)
            dfs(root.right, cur_max)

        dfs(root.left, root.val)
        dfs(root.right, root.val)

        return count