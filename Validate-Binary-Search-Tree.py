# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # # 1. Depth First Search with recursion
        # # Defining helper function to compare
        # def valid(node, lower, upper):
        #     # Empty tree is considered as BST 
        #     if not node:
        #         return True
        #     # If node value does not lie in boundaries, return False
        #     if not (node.val > lower and node.val < upper):
        #         return False
            
        #     # Calling recrusively with UPDATED BOUNDARIES to check subtrees 
        #     return (valid(node.left, lower, node.val) and valid(node.right, node.val, upper))

        # # Calling helper function on root with boundaries as -inf and inf
        # return valid(root, float("-inf"), float("inf"))

        # 2. Breadth First Search

        queue = deque([(root, float('-inf'), float("inf"))])

        while queue:
            node, left, right = queue.popleft()

            if not node:
                return True

            if not (left < node.val < right):
                return False
            
            if node.left:
                queue.append((node.left, left, node.val))
            if node.right:
                queue.append((node.right, node.val, right))
        return True


