# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        # # If root not present return none
        # if not root:
        #     return None
        
        # # Compare key value with current node value
        # if key > root.val:
        #     root.right = self.deleteNode(root.right, key) #if key is greater than current val, calling deleteNode on right subtree
        # elif key < root.val: 
        #     root.left = self.deleteNode(root.left, key) #if key is less, calling deleteNode on left subtree with key
        # else:
        #     if not root.left: #if left subtree is not present, return right subtree
        #         return root.right
        #     elif not root.right: # if right subtree not present, return left subtree
        #         return root.left

        #     # We reached here means, found the node with key value
        #     # Finding min in right subtree of root
        #     curr = root.right
        #     while curr.left:
        #         curr = curr.left
        #     root.val = curr.val
        #     root.right = self.deleteNode(root.right, root.val)
        # return root

    def helper(self, root):
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        right = root.right
        left = root.left
        # find largest on left
        while left.right:
            left = left.right
        left.right = right
        return root.left
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            return self.helper(root)
        curr = root
        while root:
            if key < root.val:
                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                root = root.right
        return curr
            

