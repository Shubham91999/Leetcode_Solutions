# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Using Recursion with DFS

        # # Checking is any of the traversal is empty 
        # if not preorder or not inorder:
        #     return None

        # # First element of preorder traversal gives us the root
        # root = TreeNode(preorder[0])

        # # Finding it in inorder to get left and right subtree nodes
        # mid = inorder.index(preorder[0])

        # # Bduilding left subtree with elements present in left of mid in inorder
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # # Building right subtree with elements present in right of mid in inorder
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root

        # 2. Using Hashmap with DFS
        # Creating hashmap, Node Value (key) -> Index in inorder (value)
        indices = {val : idx for idx, val in enumerate(inorder)}

        # Variable pre_idx for creating new node with value from preorder
        # Declared as self.pre_idx to retain value across all the recursive calls
        self.pre_idx = 0

        # Function to construct tree 
        def dfs(l, r):
            if l > r:
                return None

            # Value to store in newly created node
            root_val = preorder[self.pre_idx]
            # Incrementing to point next element in preorder
            self.pre_idx += 1
            # Creating new node with value taken from preorder
            root = TreeNode(root_val)
            # Getting index from hashmap for 
            mid = indices[root_val]

            # Calling dfs for building left subtree, l = starting to mid-1 in inorder
            root.left = dfs(l, mid - 1)

            # Calling dfs for building right subtree, mid+1 = starting to r = end in inorder
            root.right = dfs(mid+1, r)

            return root

        return dfs(0, len(inorder) - 1)



