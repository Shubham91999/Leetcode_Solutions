class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visited = set()
        visiting = set()
        order = []

        def dfs(crs: int) -> bool:
            if crs in visited:
                return True
            if crs in visiting: 
                return False
            visiting.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            order.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return order