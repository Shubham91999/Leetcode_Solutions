# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def deleteNode(self, root: Optional[TreeNode], key: int)-> Optional[TreeNode]:
        # 1. Recursion
        #     # Checking base condition, if root present or not
        #     if not root:
        #         return None
        #     if key < root.val:
        #         root.left = self.deleteNode(root.left, key) # If value to be deleted is in left subtree     
        #     elif key > root.val:
        #         root.right = self.deleteNode(root.right, key) # If value to be deleted is in right subtree
        #     # Key is not less or greater than root value, it means we found the value to be deleted
        #     else:
        #         # Root found with only one child
        #         if not root.left:
        #             return root.right 
        #         elif not root.right:
        #             return root.left
        #         # Root found with both children
        #         """In this case we have two options
        #         1) Find minimum from right subtree  
        #         2) Find maximum from left subtree
        #          """
        #         curr = root.right  # Assigning root's right subtree to curr as we are going to get minimum from right subtree
        #         while curr.left:
        #             curr = curr.left # Minimum from right subtree found
        #         root.val = curr.val # Replacing root's value with minimum from right subtree
        #         # Now, there will be two nodes with same value, to avoid duplication
        #         # call delete on right subtree as we found minimum from right with root value
        #         root.right = self.deleteNode(root.right, root.val)

        #     return root

        # 2. Iteration
            if not root:
                return None
            # Node to be deleted found at root position
            if root.val == key:
                return self.helper(root) # Helper function will join two hanging subtree after deleteion of root node

            curr = root # Storing reference in case key not found in tree

            # Key not found at root, searching in left or right subtree
            while root:
                # Key is lesser than root node
                if key < root.val:
                    # If found in left subtree, call helper with root left
                    if root.left and root.left.val == key:
                        root.left = self.helper(root.left)
                        break
                    root = root.left # Checking iteratively in left subtree
                else:
                    # in else, it means key is greater than root node
                    if root.right and root.right.val == key:
                        root.right = self.helper(root.right)
                        break
                    root = root.right
            return curr

        def helper(self, root):
            if not root.left:
                return root.left
            if not root.right:
                return root.left
            # Both children present for root(to be deleted) node
            left = root.left # Taking ref of left subtree 
            right = root.right # Taking ref of right subtree 

            # We are going to attached right subtree to the max node in left subtree
            # Finding max node from left subtree
            while left.right:
                left = left.right # Now, left points to the max (rightmost) node in left subtree
            left.right = right # Attaching right subtree to max in left
            return root.left # returning root's left as we have attached right subtree in it



        