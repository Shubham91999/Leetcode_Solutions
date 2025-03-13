# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res=[]
        while queue:
            rightmost = None
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    rightmost = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightmost:
                res.append(rightmost.val)
        return res

        # res = []
        # def dfs(root, depth):
        #     if not root:
        #         return None
        #     if depth == len(res):
        #         res.append(root.val)
        #     dfs(root.right, depth+1)
        #     dfs(root.left, depth+1)
        # dfs(root, 0)
        # return res