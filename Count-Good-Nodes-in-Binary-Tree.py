# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # self.res = 0
        # def dfs(root, maxVal):
        #     if not root:
        #         return 0
        #     if root.val >= maxVal:
        #         self.res += 1
        #         maxVal = root.val

        #     dfs(root.left, maxVal)
        #     dfs(root.right, maxVal)
        #     return self.res
        # return dfs(root, root.val)

        if not root:
            return 0

        queue = deque()
        queue.append((root, float('-inf')))
        res = 0
        while queue:
            node, maxVal = queue.popleft()
            if node.val >= maxVal:
                res += 1
            if node.left:
                queue.append((node.left, max(maxVal, node.val)))
            if node.right:
                queue.append((node.right, max(maxVal, node.val)))
        return res



