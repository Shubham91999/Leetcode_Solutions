class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. DFS (Recursion)
        # Edge case
        # if not n:
        #     return False

        # adj = defaultdict(list)
        # for i, j in edges:
        #     # Appending twice as edges are undirected 
        #     adj[i].append(j)
        #     adj[j].append(i)

        # visit = set()
        # def dfs(cur, prev):
        #     if cur in visit:
        #         return False
        #     visit.add(cur)
        #     for nei in adj[cur]:
        #         if nei == prev:
        #             continue
        #         if not dfs(nei, cur):
        #             return False
        #     return True
        
        # return dfs(0, -1) and len(visit) == n

        # 2. BFS (Queue)
        if len(edges) > n - 1:
            return False
        adj = [[] for i in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()
        q = collections.deque()
        q.append((0, -1)) # (current node, parent node)
        visit.add(0)

        while q:
            cur, prev = q.popleft()
            for nei in adj[cur]:
                if nei == prev:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, cur))
        return len(visit) == n