class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        inorder = [0] * numCourses

        for u, v in prerequisites:
            adj[v].append(u)
            inorder[u] += 1

        queue = deque()
        for num in range(numCourses):
            if inorder[num] == 0:
                queue.append(num)
                
        taken = 0
        while queue:
            cur = queue.popleft()
            taken += 1
            for nei in adj[cur]:
                inorder[nei] -= 1
                if inorder[nei] == 0:
                    queue.append(nei)

        return taken == numCourses



 

        
