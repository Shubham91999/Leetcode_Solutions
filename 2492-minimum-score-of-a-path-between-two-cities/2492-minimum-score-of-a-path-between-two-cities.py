class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Building adjacency matrix
        adj = defaultdict(list)
        for src, dest, dist in roads:
            adj[src].append(dest)
            adj[dest].append(src)

        # Set to maintain the reachable nodes
        reachable = set()

        # DFS to populate reachable set
        def dfs(node: int) -> None:
            reachable.add(node)
            for nei in adj[node]:
                if nei not in reachable:
                    dfs(nei)

        # calling the dfs 
        dfs(1)

        min_dist = float('inf')
        for src, dest, dist in roads:
            if src in reachable and dest in reachable:
                min_dist = min(min_dist, dist)

        return min_dist      


        