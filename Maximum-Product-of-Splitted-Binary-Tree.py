from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # 1. DFS One Pass
        """
        subtree_1_sums = []
        max_product = 0
        MOD = 10 ** 9 + 7

        # helper to calculate the sum of tree
        def sumTree(root: Optional[TreeNode]) -> int:
            # edge case: not root present
            if not root:
                return 0
            left = sumTree(root.left)
            right = sumTree(root.right)
            res = root.val + left + right
            subtree_1_sums.append(res)
            return res

        # Get total sum of the tree
        # Get sum of subtrees in a list
        total_sum = sumTree(root)
        # Calculate sum of subtree 2
        for subtree_1_sum in subtree_1_sums:
            subtree_2_sum = total_sum - subtree_1_sum
        # Calculate and maintain the mazimum product
            max_product = max(max_product, subtree_1_sum * subtree_2_sum)
        # return max product
        return max_product % MOD
        """

        # 2. DFS Two Pass (no list memory)
        MOD = 10 ** 9 + 7

        # First Pass
        # calculating total sum of tree
        def sumTree(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return root.val + sumTree(root.left) + sumTree(root.right)
        total = sumTree(root)

        # Second Pass
        # compute subtree sums and max product
        best = 0
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal best 
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            subtree_sum = left + right + root.val

            best = max(best, subtree_sum * (total - subtree_sum))

            return subtree_sum

        dfs(root)
        return best % MOD

 
     