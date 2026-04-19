"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        """
        if not node:
            return None
        oldToNew = {}

        def dfs(node: Optional["Node"]) -> Optional["Node"]:
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)
        """

        # BFS
        if not node:
            return None 

        oldToNew = {}
        queue = deque([node])
        new_node = Node(node.val)
        oldToNew[node] = new_node

        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    copy = Node(nei.val)
                    oldToNew[nei] = copy
                    queue.append(nei)
                oldToNew[cur].neighbors.append(oldToNew[nei])

        return new_node