"""
- The basic intuition I am getting over here is:
- If we start from the root node, then we should go down till the leaf node.
- While going down, we should maintain the values so that once it reaches the leaf node, it will not have any children.
- At the end, right, if it doesn't have left or right, then that means it's a leaf.
- In that case, whatever the sequence or the values that we have found, we need to make an integer out of it, and then similarly we can backtrack to the previous location.
We will have 10, and then we'll go to 1. That means then you will have 101, so whatever the binary to integer for that. Again it will go back, but as we have explored both left and right children, again it will go back to 1, which is a root node. It will go to the right one, which is 11, and then 110111.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def helper(node, num):
            if not node:
                return 0
            num = (num * 2) + node.val
            if not node.left and not node.right:
                return num
            return helper(node.left, num) + helper(node.right, num)
        
        return helper(root, 0)

        