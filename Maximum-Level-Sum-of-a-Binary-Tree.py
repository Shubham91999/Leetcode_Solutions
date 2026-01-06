# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import defaultdict, deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total_map = defaultdict(list)

        q = deque([root])
        level = 1

        while q:
            cur_total = 0
            for _ in range(len(q)):
        
                cur = q.popleft()
                cur_total += cur.val

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            total_map[cur_total].append(level)
            level += 1

        print(total_map)
        max_total = root.val
        res = 1

        for total, level in total_map.items():
            if total > max_total:
                max_total = total
                res = total_map[total][0]

        return res

            




