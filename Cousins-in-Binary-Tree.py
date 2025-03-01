# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        # Dictionary to maintain val : parent, depth
        tracker = {}

        # DFS to traverse all the nodes and get their depth and parent
        def dfs(node, parent, depth, x, y):
            if not node:
                return 

            dfs(node.left, node, depth+1, x, y)
            dfs(node.right, node, depth+1, x, y)

            # Storing parent and depth of current node, if value matches with either x or y
            if node.val in (x,y):
                # Key is node's value : Value (parent, depth)
                tracker[node.val] = (parent, depth)

        # calling function to traverse from root
        dfs(root, None, 0, x,y)

        # Checking required conditions are storing boolean result in cousins variable
        cousins = tracker.get(x) and tracker.get(y) and tracker[x][1] == tracker[y][1] and tracker[x][0] != tracker[y][0]

        return cousins

        
        