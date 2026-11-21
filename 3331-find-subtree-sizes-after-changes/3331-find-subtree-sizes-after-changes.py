"""
- Tree -> 0 to n-1 nodes
- parent -> parent[i] is parent of node i
- node 0 (root) -> parent[0] == -1
- s string with same length as n
- s[i] assigned to node i

- Changes made for all nodes from 1 to n-1:
    - Closest node y to node x -> y is an ancestor/parent of x and s[x] == s[y]
        - for every x find y, if its the parent of x and both x,y have same value in s
    - node y doesnt exist, do nothing
    - if node y is present, remove edge between x and its current parent
        - make y its new parent b adding an edge between them 

- Return list answer, size n -> answer[i] is the size of subtree rooted at node i in final tree

"""

class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        children = [[] for _ in s]
        for x in range(1, len(s)):
            children[parent[x]].append(x)
        size, last = [1] * len(s), {}  # last[c]: the deepest node with letter c on the path from the root

        def dfs(x: int) -> None:
            c = s[x]
            above = last.get(c, -1)  # the closest ancestor with the same letter, or -1
            last[c] = x
            for child in children[x]:
                dfs(child)
            last[c] = above
            if x:  # the root has no parent
                size[above if above >= 0 else parent[x]] += size[x]

        dfs(0)
        return size