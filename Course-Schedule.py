class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. DFS Recursively
        # Hashmap to map courses -> prerequisites list
        # preMap = {i: [] for i in range(numCourses)}  
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)

        # visited = set() # To store all visited courses

        # def dfs(crs):
        #     # First checking the base cases
        #     if crs in visited: # if in visited set, it means we are visiting the same course twice, loop detected
        #         return False
        #     if preMap[crs] == []: # if course has no prerequsites left
        #         return True

        #     visited.add(crs) # Adding that course in visited set
        #     for pre in preMap[crs]: # For every preq in list of preq for current course
        #         if not dfs(pre): # if dfs return False, return False
        #             return False

        #     visited.remove(crs)
        #     preMap[crs] = []
        #     return True

        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True

        # 2. Kahn's Algorithm (Topological Sort)
        indegree = [0] * numCourses  # List to store number of prereq required for course/index [0, 1, 3, 2, 0, 1]
        adj = [[] for i in range(numCourses)]  # List of courses that depend on course i  [[1], [2], [3], []]

        # Initializing indegree and adjacency list
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        # Appending courses (index) with indegree 0 in queue
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for neighbor in adj[node]: # Visiting neighbor nodes/connected courses for node popped from queue
                indegree[neighbor] -= 1 # Decrementing indegree of the neighbor node
                if indegree[neighbor] == 0: # After decrementing, if indegree is 0, append in queue
                    q.append(neighbor)
        return finish == numCourses  # if finish and numcourses same, return True






        