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

        # List to store result 
        res = []

        # Queue to maintain level
        q = collections.deque()
        #Enqueuing queue with root node
        q.append(root)

        # Loop to iterate till q is empty
        while q:
            qLen = len(q)
            # List to maintain all elements at particular level
            level = []

            for i in range(qLen):
                # Popping the leftmost node
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)
        return res

            



        