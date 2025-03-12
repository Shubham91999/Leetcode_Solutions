# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # 1 . Brute Force Approach with O(n^2)
    #     if not root:
    #         return True
    #     left_depth = self.maxDepth(root.left)
    #     right_depth = self.maxDepth(root.right)
    #     if abs(left_depth - right_depth) > 1:
    #         return False
    #     else:
    #         return self.isBalanced(root.left) and self.isBalanced(root.right)    
    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #     else:
    #         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # 2. Depth First Search
        def dfs(root)-> [bool, int]:
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]