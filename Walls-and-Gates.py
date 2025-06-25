class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        rows, cols = len(rooms), len(rooms[0])
        visit = set()
        q = collections.deque()

        def addRoom(r, c):
            if (r not in range(rows)) or (c not in range(cols)) or (rooms[r][c]==-1) or ((r, c) in visit):
                return 
            
            q.append((r, c))
            visit.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0 and (r, c) not in visit:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist += 1
            