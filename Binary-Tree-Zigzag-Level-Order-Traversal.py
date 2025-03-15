# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        level_count = 0
        while queue:
            curr_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    curr_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_count % 2 == 0:
                res.append(curr_level)
            else:
                res.append(curr_level[::-1])
            level_count += 1
        return res[:-1]


            