# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # def dfs(node):
        #     elements = []

        #     # Visit left
        #     if node.left:
        #         elements += dfs(node.left)
        #     # Visit base
        #     elements.append(node.val)
        #     # Visit right
        #     if node.right:
        #         elements += dfs(node.right)
            
        #     return elements

        # result = dfs(root)
        # #print(result[k-1])
        # return result[k-1]
            
        # Morris Traversal
        curr = root

        # Iterate for all nodes in tree
        while curr:
            """ If root doesn't have left subtree, 
            visit current node while decrementing counter and if 0 return current.val """
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                """ If left subtree present,
                get inorder predecessor of root
                then check pred's right
                """
                pred = curr.left
                # After this loop we will get the rightmost node in left subtree of current node giving us inorder predecessor
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    # Pred's right present, assign null to it
                    pred.right = None
                    # Visit node, decrementing counter
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        return -1


                
                

        

        