# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- DFS should provide back sum of nodes and number of nodes
- Add result of left subtree dfs and result of right subtree dfs
- Add number of nodes from left and right dfs
- Add current value to dfs total result 
- Add 1 to number of nodes
- avg = result / number of nodes
- if avg equal to current value
    - count += 1
"""
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        # dfs returns -> [total, number of nodes]
        def dfs(root: Optional['TreeNode'], total: int, nodes: int) -> List[int]: 
            nonlocal count

            if not root:
                return [0, 0]

            leftTotal, leftNodes = dfs(root.left, total + root.val, nodes + 1)
            rightTotal, rightNodes = dfs(root.right, total + root.val, nodes + 1)

            total = leftTotal + rightTotal + root.val
            nodes = leftNodes + rightNodes + 1
            avg = total // nodes

            if avg == root.val:
                count += 1

            return [total, nodes]

        dfs(root, 0, 0)
        return count


            


