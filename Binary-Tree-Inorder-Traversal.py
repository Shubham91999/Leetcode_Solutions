# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []

        # def dfs(root):

        #     if not root:
        #         return None

        #     # Visit left node
        #     dfs(root.left)
        #     # Visit current node
        #     res.append(root.val)
        #     # Visit right node
        #     dfs(root.right)

        # dfs(root)
        # return res

        res = []

        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res




        