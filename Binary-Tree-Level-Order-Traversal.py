# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []

        # def dfs(node, depth):
        #     if not node:
        #         return None
        #     if len(res) == depth:
        #         res.append([])
            
        #     res[depth].append(node.val)
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        
        # dfs(root, 0)
        # return res

        # Using Breadth First Search

        # Result list to store the result
        res = []

        #Using deque to implement queue
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            # Loop will start from 0 and will iterate till the length of queue
            for i in range(qLen):
                #Popping the elements from queue
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                    res.append(level)
        return res



        