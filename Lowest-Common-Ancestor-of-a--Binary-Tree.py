# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case
        if not root:
            return None
        # Found atleast one of the target
        if root == p or root == q: 
            return root 

        l = self.lowestCommonAncestor(root.left, p , q) # Non-null if p or q or their LCA found in left subtree
        r = self.lowestCommonAncestor(root.right, p, q) # Non-null if p or q or their LCS found in right subtree

        if l and r: # Both non-null, it means one target found in each subtree, that means current root is their LCA
            return root
        else:
            return l or r # whichever side is non-null carries the info of either a found target or the LCA deeper in that subtree
    

        
                
