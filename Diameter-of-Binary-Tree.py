# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 1. Brute Force with o(n^2)
    #     if not root:
    #         return 0

    #     leftHeight = self.maxHeight(root.left)
    #     rightHeight = self.maxHeight(root.right)
    #     diameter = leftHeight + rightHeight

    #     sub = max(self.diameterOfBinaryTree(root.left),
    #     self.diameterOfBinaryTree(root.right))

    #     return max(diameter, sub)

    # def maxHeight(self, root: Optional[TreeNode])-> int:
    #     if not root:
    #         return 0

    #     return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

    # 2. Depth First Search with Recursion

        self.res = 0
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        dfs(root)
        return self.res


        

