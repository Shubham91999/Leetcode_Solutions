# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Recursion (DFS)
        # # If both trees null, return True
        # if not p and not q:
        #     return True
        
        # # If one of the tree is null or values not same, return False
        # if not p or not q or p.val != q.val:
        #     return False

        # # Recursive call to check subtrees
        # return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        # Iterative DFS (Using stack)
        # Initializing stack
        stack = [(p, q)] # Tree refs assigned as tuple 

        # Pop nodes till stack has elements
        # while stack:
        #     node1, node2 = stack.pop()

        #     # if both nodes null, skip the iteration to check remaining nodes
        #     if not node1 and not node2:
        #         continue
        #     # if one of the node is null and value is differenr, return false
        #     if not node1 or not node2 or node1.val != node2.val:
        #         return False

        #     # Add child nodes for further comparision
        #     stack.append((node1.left, node2.left))
        #     stack.append((node1.right, node2.right))

        # return True

        # 3. Iterative BFS (Queue)
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                node1 = q1.popleft()
                node2 = q2.popleft()

                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False

                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
        return True

