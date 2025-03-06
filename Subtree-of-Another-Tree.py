# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "N"
            return f"({node.val}, {serialize(node.left)}, {serialize(node.right)})"

        r = serialize(root)
        sr = serialize(subRoot)
        return sr in r




    #     # Taking care of base cases
    #     # If given subtree is empty
    #     if not subRoot:
    #         return True
        
    #     # Checking main tree (as subtree is already checked, not checking again)
    #     if not root:
    #         return False

    #     # If both conditions are not met, it means both trees are present, compare further
        
    #     # Calling sameTree function on root node and given subtree
    #     if self.sameTree(root, subRoot):
    #         return True

    #     # Calling subTree function recrusively on children of root tree and given subtree
    #     return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


        
    # # Writing a helper function to compare the trees
    # def sameTree(self, s: TreeNode, t: TreeNode) -> bool:
    #     # Checking if both trees are empty
    #     if not s and not t:
    #         return True

    #     # Now, we know both trees are not empty
    #     # Making sure both trees have values and the values are same
    #     if s and t and s.val == t.val:
    #         # above we checked only current node, we also need to compare their child nodes
    #         # Recursive call to check subtrees 
    #         return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))

    #     return False