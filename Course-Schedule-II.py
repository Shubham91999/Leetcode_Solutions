class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Cycle Detection DFS
        # Build an adjacency list
        # prereq = {c: [] for c in range(numCourses)}
        # for crs, pre in prerequisites:
        #     prereq[crs].append(pre)

        # # A course has 3 possible states:
        # # 1. Visited -> course has been added to output list
        # # 2. Visiting -> Course not added to output, but added to cycle
        # # 3. Unvisited -> Course not added to output or cycle
        # output = []
        # visit, cycle = set(), set()
        # # Passing currently visiting course to dfs
        # def dfs(crs):
        #     if crs in cycle:  # If crs already visited in current cycle
        #         return False
        #     if crs in visit:  # If course is already visited and not needed to visit again
        #         return True
        #     cycle.add(crs)  # Maintaining current cycle
        #     for pre in prereq[crs]:  # DFS on all prereqa of current course
        #         if not dfs(pre):
        #             return False

        #     cycle.remove(crs) # Cycle is completed, when all prereqs for current course are visited, and not cycle found
        #     visit.add(crs)
        #     output.append(crs)
        #     return True
        
        # # Running dfs for every course in numCourses
        # for c in range(numCourses):
        #     if not dfs(c):  # If cycle detected, dfs returns false, so return an empty list
        #         return []
        # return output

        # 2. Topological Sort DFS
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)

        output = []
        def dfs(crs):
            output.append(crs)
            indegree[crs] -= 1
            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        return output if len(output) == numCourses else []


