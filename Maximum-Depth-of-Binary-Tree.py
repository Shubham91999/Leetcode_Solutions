# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. Iterative BFS (Using Queue)
        # if not root:
        #     return 0
        # queue = deque([root])
        # level = 0

        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)      
        #     level += 1

        # return level

        # # 2. Iterative DFS (Stack)
        # if not root:
        #     return 0
        # stack = [[root, 1]]
        # res = 1

        # while stack:
        #     node, depth = stack.pop()

        #     res = max(res, depth)
        #     if node.left:
        #         stack.append([node.left, depth + 1])
        #     if node.right:
        #         stack.append([node.right, depth + 1])

        # return res

        # 3. Recursion
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))