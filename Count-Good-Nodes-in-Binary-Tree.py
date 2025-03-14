# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 1. DFS Recursion
        # def dfs(root, maxVal):
        #     if not root:
        #         return 0
        #     res = 1 if root.val >= maxVal else 0
        #     maxVal = max(maxVal, root.val)
        #     res += dfs(root.left, maxVal)
        #     res += dfs(root.right, maxVal)
        #     return res
        # return dfs(root, float('-inf'))

        # 2. DFS Recursion with global variable
        # self.count = 0
        # def dfs(root, maxVal):
        #     if not root:
        #         return 0
        #     if root.val >= maxVal:
        #         self.count += 1
        #         maxVal = root.val
        #     dfs(root.left, maxVal)
        #     dfs(root.right, maxVal)
        #     return self.count
        # return dfs(root, float('-inf'))

        # 3. BFS with Queue
        if not root:
            return None
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


